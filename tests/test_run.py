from io import BytesIO

from PIL import Image

from run import app


def make_image(image_format: str) -> BytesIO:
    image = Image.new("RGB", (4, 4), color="red")
    buffer = BytesIO()
    image.save(buffer, format=image_format)
    buffer.seek(0)
    return buffer


def test_resized_png_stays_png() -> None:
    app.config["TESTING"] = True

    with app.test_client() as client:
        response = client.post(
            "/",
            data={
                "image": (make_image("PNG"), "sample.png"),
                "width": "2",
                "height": "2",
                "quality": "85",
            },
            content_type="multipart/form-data",
        )

    assert response.status_code == 200
    assert response.mimetype == "image/png"

    output = Image.open(BytesIO(response.data))
    assert output.format == "PNG"
    assert output.size == (2, 2)

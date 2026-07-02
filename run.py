from flask import Flask, render_template, request, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)


# index
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        image_file = request.files.get("image")
        width = request.form.get("width")
        height = request.form.get("height")
        quality = request.form.get("quality")

        if not image_file:
            return "Did not receive an Image"

        img = Image.open(image_file)
        output_format = "PNG" if img.format == "PNG" else "JPEG"

        if width and height:
            img = img.resize((int(width), int(height)), Image.Resampling.LANCZOS)

        # buffer
        buffer = BytesIO()
        quality = int(quality) if quality else 85

        save_options = {"format": output_format, "optimize": True}
        if output_format == "JPEG":
            save_options["quality"] = quality
        img.save(buffer, **save_options)
        buffer.seek(0)
        # file.jpg => opt_file.jpg
        return send_file(
            buffer,
            as_attachment=True,
            download_name="opt_" + image_file.filename,
            mimetype="image/png" if output_format == "PNG" else "image/jpeg",
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run()

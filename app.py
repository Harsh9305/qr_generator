from flask import Flask, send_file, request
import qrcode
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <h1>QR Code Generator</h1>
        <form action="/generate" method="get">
            <label for="data">Data to encode:</label>
            <input type="text" id="data" name="data" required>
            <button type="submit">Generate QR Code</button>
        </form>
    '''

@app.route('/generate')
def generate_qr():
    data = request.args.get('data')
    if not data:
        return "Error: No data provided.", 400

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an in-memory image (not saving to file)
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to a BytesIO object
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Send the image directly as a response
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


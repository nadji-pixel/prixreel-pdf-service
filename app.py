from flask import Flask, request, jsonify, send_file
from weasyprint import HTML
import io
import os

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "alive"})

@app.route('/pdf', methods=['POST'])
def generate_pdf():
    try:
        data = request.get_json()
        if not data or 'html' not in data:
            return jsonify({"error": "Missing 'html' field"}), 400

        html_content = data['html']

        # Générer le PDF en mémoire
        pdf_bytes = HTML(string=html_content).write_pdf()

        # Retourner le PDF directement
        buf = io.BytesIO(pdf_bytes)
        buf.seek(0)
        return send_file(
            buf,
            mimetype='application/pdf',
            as_attachment=False,
            download_name='rapport.pdf'
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

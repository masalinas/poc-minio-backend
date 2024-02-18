from io import BytesIO

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
from flask import Response

from minio import Minio
from minio.error import S3Error

app = Flask(__name__)
CORS(app)

_client = Minio("localhost:9000",
    access_key="BsvW9jlpYX8TvD9F",
    secret_key="HrGdJapKsXbKEcXABWNQ2CO15v3y9MMk",
    cert_check=False
)

_bucket_name = "uniovi"

@app.route("/upload", methods=["POST"])
def upload_files():
    # Make the bucket if it doesn't exist.    
    found = _client.bucket_exists("uniovi")
    if not found:
        _client.make_bucket(_bucket_name)
        print("Created bucket", _bucket_name)
    else:
        print("Bucket", _bucket_name, "already exists")

    # Get the list of files from webpage 
    files = request.files.getlist("file[]")

    for file in files: 
        # save locally
        #file.save(file.filename)
        
        # get raw and lenfth file
        raw_img = BytesIO(file.read())
        raw_img_size = raw_img.getbuffer().nbytes

        # Upload the file, renaming it in the process
        _client.put_object(bucket_name=_bucket_name, object_name=file.filename, data=raw_img, length=raw_img_size)
    
    return {}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5001", debug=True)
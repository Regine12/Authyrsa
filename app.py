from flask import Flask, render_template, request
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)

# Generate RSA key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Convert keys to PEM format
private_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':
        message = request.form['message']

        encrypted = public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        encrypted_message = encrypted.hex()

        return {
            'encrypted': encrypted_message
        }

    return render_template('encrypt.html')

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':
        encrypted_message = request.form['encrypted']

        decrypted = private_key.decrypt(
            bytes.fromhex(encrypted_message),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        decrypted_message = decrypted.decode('utf-8')

        return {
            'decrypted': decrypted_message
        }

    return render_template('decrypt.html')

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template, request, jsonify
# from cryptography.hazmat.primitives.asymmetric import rsa, padding
# from cryptography.hazmat.primitives import serialization, hashes
# from cryptography.hazmat.backends import default_backend

# app = Flask(__name__)

# # Generate RSA key pair
# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
#     backend=default_backend()
# )
# public_key = private_key.public_key()

# # Encryption route
# @app.route('/encrypt', methods=['POST'])
# def encrypt():
#     message = request.form['message']

#     encrypted = public_key.encrypt(
#         message.encode('utf-8'),
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )

#     encrypted_message = encrypted.hex()

#     return jsonify({'encrypted': encrypted_message})

# # Decryption route
# @app.route('/decrypt', methods=['POST'])
# def decrypt():
#     encrypted_message = request.form['encrypted']

#     decrypted = private_key.decrypt(
#         bytes.fromhex(encrypted_message),
#         padding.OAEP(
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),
#             algorithm=hashes.SHA256(),
#             label=None
#         )
#     )

#     decrypted_message = decrypted.decode('utf-8')

#     return jsonify({'decrypted': decrypted_message})

# if __name__ == '__main__':
#     app.run()


# from flask import Flask, render_template, request, jsonify
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP

# app = Flask(__name__)

# # Generate RSA key pair
# key = RSA.generate(2048)
# public_key = key.publickey().export_key().decode()
# private_key = key.export_key().decode()

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/encrypt', methods=['GET', 'POST'])
# def encrypt():
#     if request.method == 'POST':
#         message = request.form['message']
#         cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
#         encrypted = cipher.encrypt(message.encode()).hex()
#         return jsonify({'encrypted': encrypted})
#     return render_template('encrypt.html')

# @app.route('/decrypt', methods=['GET', 'POST'])
# def decrypt():
#     if request.method == 'POST':
#         encrypted = bytes.fromhex(request.form['encrypted'])
#         cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
#         decrypted = cipher.decrypt(encrypted).decode()
#         return jsonify({'decrypted': decrypted})
#     return render_template('decrypt.html')

# if __name__ == '__main__':
#     app.run()

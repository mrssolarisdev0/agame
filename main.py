from cryptography.fernet import Fernet

def encrypt_this(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_this(message, key):
    fernet = Fernet(key)
    return fernet.decrypt(message).decode()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = b'h0WBu417FzdD2pFcSz-tq2I5hVPopuKfFlTN_WGN5UQ=' # Ah é, a mensagem é uma string codificada em base 64.
    message = "A mensagem aqui"
    decrypted_message = decrypt_this(message, key)
    print('Mensagem decriptada:', decrypted_message)

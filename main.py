from cryptography.fernet import Fernet

def encrypt_this(message, key):
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_this(message, key):
    fernet = Fernet(key)
    return fernet.decrypt(message).decode()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = b'achaveaqui' # Ah é, a mensagem é uma string codificada em base 64 5x (foi só pra ficar do tamanho certo :c ).
    message = "A mensagem aqui"
    decrypted_message = decrypt_this(message, key)
    print('Mensagem decriptada:', decrypted_message)

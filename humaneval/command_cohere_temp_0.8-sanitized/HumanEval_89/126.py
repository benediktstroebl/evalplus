def encrypt(s):
    encrypted = ''
    rotating_letters = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'efghijnopqrstuvwxyzabcd')
    encrypted = s.translate(rotating_letters)
    return encrypted
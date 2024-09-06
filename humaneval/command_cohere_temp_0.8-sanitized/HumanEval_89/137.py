def encrypt(s):
    encrypted = ''
    rotating_letters = str.maketrans('abcdefghijklmnopqrstuvwxyz',
                                      'efghijklmnopqrstuvwxyz abcdefg hijklmnopqrstuv abcdefg hijklmnop')
    encrypted = s.translate(rotating_letters)
    return encrypted
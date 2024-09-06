def encrypt(s):
    encrypted = ''
    rotating_letter = s[0]
    for letter in s:
        if letter != rotating_letter:
            rotating_letter = letter
            encrypted += rotating_letter
            rotating_letter = rotating_letter + 2
            if rotating_letter > 'z':
                rotating_letter = 'a'
        else:
            encrypted += rotating_letter
    return encrypted
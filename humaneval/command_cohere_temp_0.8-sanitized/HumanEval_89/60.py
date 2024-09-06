def encrypt(s):
    encrypted = ''
    rotating_letter = s[0]
    for letter in s:
        if letter != rotating_letter:
            encrypted += rotating_letter
            rotating_letter = letter
        else:
            rotating_letter = rotating_letter + 1
    if rotating_letter != s[len(s) - 1]:
        encrypted += rotating_letter
    return encrypted
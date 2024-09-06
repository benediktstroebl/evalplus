ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
def shift_alphabet(s):
    return "".join([ALPHABET[((ord(ch) + 5) % 26)] for ch in s])
def decode_shift(s):
    return shift_alphabet(s)
def decode_shift(s: str):
    return "".join([chr(int(c)-97 + 'a') for c in s])
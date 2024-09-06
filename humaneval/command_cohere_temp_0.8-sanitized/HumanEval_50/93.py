def decode_shift(s: str):
    return s.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", " abcdefghijklmnopqrstuvwxyz"))
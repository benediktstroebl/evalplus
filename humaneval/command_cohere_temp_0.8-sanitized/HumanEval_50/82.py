def decode_shift(s: str):
    return s[:, :-5].translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ijklmnopqrstvwxyzabc'))
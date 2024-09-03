def decode_shift(s: str):
    return "".join([chr(ord(ch) - ord("a")) for ch in s])
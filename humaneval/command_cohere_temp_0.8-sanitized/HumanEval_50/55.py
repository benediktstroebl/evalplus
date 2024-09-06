def decode_shift(s: str):
    return "".join([chr(((((ord(ch) - 96) % 26) + 96) % 26) + ord("a")) for ch in s])
def decode_shift(s: str):
    """
    Decodes a string encoded with the encode_shift function.
    """
    reverse_alphabet = "abcdefghijklmnopqrstuvwxyz"
    return "".join([reverse_alphabet[ord(ch) - ord(reverse_alphabet["a"]) + ord("a")]] for ch in s)
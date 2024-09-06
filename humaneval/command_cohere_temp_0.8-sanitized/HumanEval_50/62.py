def decode_shift(s: str):
    """
    Decodes an input string encoded with the encode_shift function.
    """
    reverse_alphabet = {chr(i): chr(i - 5) for i in range(97, 123)}
    return "".join(reverse_alphabet.get(ch, ch) for ch in s)
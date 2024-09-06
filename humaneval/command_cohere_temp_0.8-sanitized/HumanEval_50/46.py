def decode_shift(s: str):
    reverse_mapping = {chr(i): chr((i - 5) % 26 + ord("a")) for i in range(97, 123)}
    return "".join(reverse_mapping.get(ch, ch) for ch in s)
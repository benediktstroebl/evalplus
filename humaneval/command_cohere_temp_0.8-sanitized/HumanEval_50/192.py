def decode_shift(s: str):
    reverse_mapping = {chr(i + ord("a")): i for i in range(97, 123)}
    return "".join([reverse_mapping.get(ch, ch) for ch in s])
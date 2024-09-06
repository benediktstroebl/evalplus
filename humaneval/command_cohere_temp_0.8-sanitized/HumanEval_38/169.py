def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    return "".join([group[1:] + group[0]] if len(group) == 3 else group for group in groups)
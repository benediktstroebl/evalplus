def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    groups = [list(group) for group in sorted(s.split(""))]
    return "".join(groups[0][i] for i in range(0, len(groups[0]), 3))
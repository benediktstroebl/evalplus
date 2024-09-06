def decode_cyclic(s: str):
    """
    Takes as input a string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3.
    groups = [s[i:i+3] for i in range(0, len(s), 3)]
    # Restore original order by reversing the cycling process.
    groups = [group[0] + group[2:] for group in groups if len(group) == 3]
    return "".join(groups)
def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function. Returns the decoded string.
    """
    # Split the encoded string into groups of three
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    # Reverse the cycling effect introduced in encoding
    groups = [group[0] + group[2:] for group in groups]
    return "".join(groups)
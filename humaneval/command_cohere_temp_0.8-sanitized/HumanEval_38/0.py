def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function. Returns the decoded string.
    """
    # Find the length of the encoded string length which is a multiple of 3.
    length = (len(s) // 3) * 3
    # Split the encoded string into groups. Each of length 3.
    groups = [s[i:i + 3] for i in range(0, length, 3)]
    # Decode each group by taking adjacent elements in a cyclic manner.
    return "".join([group[1:] + group[0]] if len(group) == 3 else group for group in groups)
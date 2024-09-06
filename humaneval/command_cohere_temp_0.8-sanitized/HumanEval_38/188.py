def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function. Returns the decoded string.
    """
    # Split string into groups. Each of length 3. 
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Remove cycling element if it's the last in the group (only one element is cyclic).
    groups = [group[:2] + group[2:] if len(group) == 4 else group for group in groups]
    return "".join(groups)
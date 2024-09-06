def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups. Each of length 3. 
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[0] + group[2:] if len(group) == 3 else group[0]) for group in groups]
    return "".join(groups)
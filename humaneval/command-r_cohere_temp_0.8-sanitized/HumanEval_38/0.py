def decode_cyclic(encoded_str: str):
    """
    Decodes a string encoded with the encode_cyclic function.
    """
    # Split the encoded string into groups of 3 characters.
    groups = [encoded_str[i:i + 3] for i in range(0, len(encoded_str), 3)]
    
    # Iterate over each group and move the first character to the end.
    decoded_groups = [''.join([group[1], group[2], group[0]]) for group in groups]
    
    # Join the decoded groups to form the original string.
    return ''.join(decoded_groups)
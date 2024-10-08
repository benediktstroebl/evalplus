def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Perform XOR operation on the integers
    result = int_a ^ int_b
    
    # Convert the result back to binary string and return it
    return bin(result)[2:]

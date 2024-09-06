def string_xor(a, b):
    """
    Performs binary XOR on two strings consisting of 1s and 0s.
    Returns the result as a string.
    """
    # translate uses str.maketrans to switch positions of '10' to '01' and vice versa
    return a.translate(str.maketrans('01', '10')) == b.translate(str.maketrans('10', '01'))
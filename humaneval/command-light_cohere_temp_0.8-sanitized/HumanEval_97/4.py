def multiply(a, b):
    """
    Function to multiply two integers and returns the product of their unit digits.
    Args:
        a:    first integer
        b:    second integer
    Returns:
        the product of their unit digits
    """
    if type(a) != int or type(b) != int:
        raise TypeError("Both numbers must be integers")
    return sum([int(x) for x in str(a)][-2:]) + sum([int(x) for x in str(b)][-2:])
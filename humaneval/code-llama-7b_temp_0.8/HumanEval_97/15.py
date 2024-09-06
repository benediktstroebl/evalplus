
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    """
    Multiply two numbers in base 10,
    keeping only the unit digit (1's place) of their product.

    Parameters:
    a (int): the first integer
    b (int): the second integer

    Returns:
    int: the unit digit (1's place) of the product

    Example:
    multiply(148, 412) should return 16.
    """
    # return (a * b) % 10

    # Another approach
    return (a % 10) * (b % 10)



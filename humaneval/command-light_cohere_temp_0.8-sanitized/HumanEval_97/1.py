def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits."""
    if type(a) != int or type(b) != int:
        raise TypeError("Both arguments must be integers.")
    return sum([int(str(x)) for x in map(str, (a + b))])
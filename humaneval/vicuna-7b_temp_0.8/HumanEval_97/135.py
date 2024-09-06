
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
    # Check that a and b are both positive integers
    if not (a > 0 and b > 0):
        return -1
    # Convert a and b to strings
    a_str = str(a)
    b_str = str(b)
    # Initialize the result to 1
    result = 1
    # Loop through the digits of a and b
    for i in range(len(a_str)):
        # Multiply the digits and add the result to the result
        result = result * 10 + int(a_str[i]) * int(b_str[i])
    return result
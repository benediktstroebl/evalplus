
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
    # Write code to complete the function
    # The method in the previous solutions is not correct.
    # We should use the idea of adding the digits in the reverse order.
    # We can use the formula (a \* b) % 10 + (a / b) \* ((a / b) % 10)
    # to compute the product of two numbers.
    return (a * b) % 10 + (a / b) * ((a / b) % 10)
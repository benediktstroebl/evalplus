
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
    # Use a while loop to find the largest digit in each number
    while len(str(a)) > len(str(b)):
        # Copy the rightmost digits of a to b
        digits = str(a)
        b_copy = str(b)
        while digits and digits[-1] == '0':
            digits = digits[:-1]
            b_copy = b_copy[:-1]
        b_copy += b_copy[::-1]
        # Check if the number of digits is the same in both b and b_copy
        if len(b_copy) != len(str(b)):
            return 0
    return int(str(a)[::-1]) * int(str(b)[::-1])

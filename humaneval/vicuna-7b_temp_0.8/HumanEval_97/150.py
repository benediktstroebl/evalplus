
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
    # First, convert the input integers to strings
    a_str = str(a)
    b_str = str(b)
    
    # Check if the units digit of the first string is 0 (11 in binary)
    if a_str[0] == '0':
        return 0
    # Check if the units digit of the second string is 0 (10 in binary)
    if b_str[0] == '0':
        return 0
    
    # Get the digits of the first number
    a_digits = [int(digit) for digit in a_str]
    # Get the digits of the second number
    b_digits = [int(digit) for digit in b_str]
    
    # Check if the second number is zero
    if len(b_digits) == 0:
        return 0
    
    # If the first number has more digits, subtract it from the second number
    if len(a_digits) > len(b_digits):
        b = [int(digit) for digit in b_digits]
        for i in range(len(b_digits), len(a_digits)):
            b.append(0)
        return sum(x * (10 ** (len(b_digits) - i - 1)) for i, x in enumerate(b))
    
    # If the first number has fewer digits than the second number,
    # pad the first number with zeroes
    b_zeros = [0] * (len(b_digits) - len(a_digits))
    a_zeros = [0] * (len(b_digits) - len(a_digits))
    a = [int(digit) for digit in a_digits + b_zeros]
    b = [int(digit) for digit in b_digits]
    
    # Check if the first number is negative
    if any([a_digits[0] < 0 for a_digits in a]) :
        a = [int(digit * (10 ** (len(a_digits) - 1)) * (10 ** (len(b_digits)

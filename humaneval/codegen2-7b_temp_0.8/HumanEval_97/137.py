
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
    result = 0
    for a_digit in a:
        a_digit_number = int(a_digit)
        b_digit_number = int(b)
        result += a_digit_number*b_digit_number
        b_digit_number = b_digit_number//10
        
    for b_digit in b:
        result += int(b_digit)*a_digit_number
        
    

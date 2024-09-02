
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
    # Multiply the last digit of each number by 10 to the power of the length of the smallest number
    # Divide the result by 10 to the power of the length of the smallest number
    a_unit_dig = a % 10
    b_unit_dig = b % 10
    
    # If either of the numbers is negative, turn it positive
    if a < 0:
        a = abs(a)
    if b < 0:
        b = abs(b)
    
    a_unit_dig_to_power = a_unit_dig * 10 ** (len(str(a)) - 1)
    b_unit_dig_to_power = b_unit_dig * 10 ** (len(str(b)) - 1)
    
    return int(a_unit_dig_to_power / 10 ** (len(str(a)) - 1)) * int(b_unit_dig_to_power / 10 ** (len(str(b)) - 1))
    


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
    # write code here
    
    # check if either number is negative
    if a < 0 or b < 0:
        return -1
    
    # check if either number is zero
    if a == 0 or b == 0:
        return 0
    
    # compute the digits of the result
    result_digits = [0] * 10
    for digit in [a % 10, b % 10]:
        result_digits[digit // 10] += digit % 10
    
    # compute the unit digits of the result
    result_unit_digits = [0] * 2
    for i in range(len(result_digits) - 1):
        if result_digits[i] == 0:
            result_unit_digits[i] = 1
            result_unit_digits[i + 1] = result_digits[i + 1]
    
    # return the product of the unit digits
    return str(sum(result_unit_digits))


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
    a_digits = number_to_list(a)
    b_digits = number_to_list(b)
    result = [0]
    
    for index, digit in enumerate(a_digits):
        result.append(digit*b_digits[index])
    
    return list_to_number(result)

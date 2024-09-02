
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
    a_str = str(a)
    b_str = str(b)
    # check if the numbers have same number of digits
    if len(a_str) == len(b_str):
        result = 0
        # iterate over the strings
        for i in range(len(a_str)):
            result += int(a_str[i]) * int(b_str[i])
        return result
    else:
        return 0

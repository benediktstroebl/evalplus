
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
    # First, convert the input integers to strings and remove the
    # decimal point
    a_str = str(a)
    b_str = str(b)
    a_str, _ = a_str.split('.')
    b_str, _ = b_str.split('.')

    # Determine the sign of the result by comparing the signs of the
    # input integers. If the first digit of the first integer is greater
    # than the first digit of the second integer, the result is positive.
    # Otherwise, the result is negative.
    if a_str[0] > b_str[0]:
        sign = 1
    else:
        sign = -1

    # Convert the input strings to integers and subtract
    a_int = int(a_str)
    b_int = int(b_str)
    result = a_int + sign * b_int

    # Convert the result to a string and format it as a two-digit
    # number with a leading 0 if necessary
    if result > 9:
        result_str = str(result)
        if result_str[1] == '0':
            result_str = result_str[0] + result_str[2:]
        result_str = "0" + result_str
        while result_str[-2:].isdigit() and result_str[-2] >= result_str[-1]:
            result_str = result_str[:-2] + "0" + result_str[-2:]

    # If the result is negative, append a minus sign at the end
    # Otherwise, the result is zero and we can return it as a string
    if sign == -1:
        result_str = "-" + result_str
    else:
        return result_str

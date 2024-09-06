
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
    a = int(a)
    b = int(b)
    a_s = str(a)
    b_s = str(b)

    a_u = a_s[1:]
    b_u = b_s[1:]

    a_u = int(a_u)
    b_u = int(b_u)

    answer = a_u * b_u

    return answer

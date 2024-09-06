
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

    if a == 0 or b == 0:
        return 0
    else:
        a_set = set(str(a))
        b_set = set(str(b))
        intersection = a_set.intersection(b_set)
        prod = 1
        for i in intersection:
            prod *= int(i)
        return prod


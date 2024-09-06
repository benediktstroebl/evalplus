
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

    for num in [a, b]:
        n = 0
        while num > 0:
            num, last_digit = divmod(num, 10)
            result += last_digit ** n
            n += 1
    return result

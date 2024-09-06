
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
    i = abs(a)
    j = abs(b)
    sum = 0
    while i >= 1 or j >= 1:
        if i % 10 > 0:
            sum = sum + j % 10 * i % 10
        i = i // 10
        j = j // 10
    return sum

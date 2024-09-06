
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
    left = int(a)
    right = int(b)
    if left == 0:
        if right == 0:
            return 0
        return 1
    if right == 0:
        return 0
    while right != 0:
        if right % 10 != left % 10:
            return 0
        right //= 10
        left //= 10
    return left

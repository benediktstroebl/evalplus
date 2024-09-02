
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
    x = int(a)
    y = int(b)
    if x == 0:
        return "0"
    if y == 0:
        return "0"
    answer = ""
    while x != 0:
        answer = str(x % 10) + answer
        x = x // 10
    while y != 0:
        answer = str(y % 10) + answer
        y = y // 10
    return answer

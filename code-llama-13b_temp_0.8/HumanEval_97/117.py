
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

    a = str(a)[::-1]
    b = str(b)[::-1]
    c = [int(a[i]) * int(b[i]) for i in range(min(len(a), len(b)))]
    # print(c)

    # c = list(map(lambda x: x * x, c))
    # c = [int(x) for x in c]
    # c = list(map(lambda x: x % 10, c))
    # c = list(map(lambda x: x * x, c))

    # print(c)

    return sum([int(x) for x in str(int(''.join(map(str, c))))])


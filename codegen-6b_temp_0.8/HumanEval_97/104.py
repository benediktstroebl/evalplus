
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
    m = a
    n = b
    l1 = [int(d) for d in str(a)]
    l2 = [int(d) for d in str(b)]

    if len(l1) > len(l2):
        l1, l2 = l2, l1

    l3 = []

    for i in range(0, len(l1)):
        val = l1[i] * l2[i]
        l3.append(val)

    if len(l3) > 0:
        product = reduce(lambda x, y: x + y, l3)
    else:
        product = 0

    return product

assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14,-15) == 20
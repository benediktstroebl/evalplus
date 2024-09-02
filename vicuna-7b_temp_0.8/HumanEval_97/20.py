
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
    # Solve the problem using two nested loops
    # Example output: 72
    units = []
    tens = []
    for i in range(10):
        units.append(str(a % 10))
        a //= 10
        tens.append(str(b % 10))
        b //= 10

    # Append the remaining digits if any
    units.append(str(a % 10))
    tens.append(str(b % 10))
    a = a // 10
    b = b // 10

    product = 0
    for i in range(len(units)):
        for j in range(len(tens)):
            product = product * (int(units[i]) + int(tens[j])) % 10
        units[i] = str(product % 10)
        tens[j] = str(product % 10)
        product = product / 10

    return ''.join(tens) + '.' + ''.join(units)

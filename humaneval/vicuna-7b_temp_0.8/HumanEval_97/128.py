
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
    # Your code here
    digit1, digit2 = map(int, input("Enter two integers separated by a space: ").split())
    unit_digits = [str(digit).zfill(2) for digit in [digit1, digit2]]
    product = 0
    for i in range(len(unit_digits)):
        if unit_digits[i] == '1':
            product *= 10
        if unit_digits[i] == '2':
            product += 2
        if unit_digits[i] == '3':
            product *= 5
        if unit_digits[i] == '4':
            product += 4
        if unit_digits[i] == '5':
            product *= 10
        if unit_digits[i] == '6':
            product += 6
        if unit_digits[i] == '7':
            product *= 10
        if unit_digits[i] == '8':
            product += 8
        if unit_digits[i] == '9':
            product *= 10
        if unit_digits[i] == '0':
            product += 0
    return product

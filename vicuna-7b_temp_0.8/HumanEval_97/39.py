
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
    # Check if the input is negative
    if a < 0:
        return -multiply(a, -b)
    # Check if the input is a power of 10
    if a == 0 or (a // 10) == a:
        return b * 10
    # Convert the input to a string of digits
    digits = str(a)
    # Create a new string with only the unit digits
    unit_digits = [d if (d % 10 == d // 10) == d // 10 else 0 for d in digits]
    # Check if the second number has only one digit
    if b == 10:
        return 1 + unit_digits[0]
    # Check if the first number is 0 or the second number is 10
    if a == 0 or b == 10:
        return 0
    # Create a temporary number for the product
    temp = 0
    # Multiply the unit digits of the first number and the second number
    for i in range(len(unit_digits)):
        if b % 10 != i:
            temp = temp * 10 + unit_digits[i]
        temp = temp * b + unit_digits[i]
    # Convert the temporary number to an integer and return the product
    return int(temp)

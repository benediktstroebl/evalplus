
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
    # Create a variable for the individual digits
    digit_a = str(a)
    digit_b = str(b)

    # Check if the input digits are zero
    if digit_a == "0" or digit_b == "0":
        return 0

    # Check if the input digits are negative
    if digit_a[0] == "-" or digit_b[0] == "-":
        # Check if the individual digits are negative
        if digit_a[1:] == "-1" or digit_b[1:] == "-1":
            return 0
        else:
            a = abs(int(digit_a))
            b = abs(int(digit_b))
    else:
        a = int(digit_a)
        b = int(digit_b)

    # Check if the input digits have different units
    if digit_a[-1] != digit_b[-1]:
        # Return 0 if the digits have different units
        return 0

    # Check if the individual digits have the same unit
    if a > b:
        # Flip the order of a and b
        a, b = b, a
    else:
        # Compare the value of a and b
        if a > b:
            # Multiply the digits and add the units
            product = 0
            for i in range(10):
                product = product * 10 + a % 10 + b // 10
                a = b // 10
            # Add the units
            product = product * 10 + a % 10
        else:
            # Multiply the digits and add the units
            product = 0
            for i in range(10):
                product = product * 10 + b % 10 + a // 10
                b = a // 10
            # Add the units
            product = product * 10 + b % 10

    return product

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
    # Check if the two input numbers are negative
    if a < 0 and b < 0:
        # If the two input numbers are negative, set the result to 0
        return 0
    # Convert the input numbers to strings
    a_str = str(a)
    b_str = str(b)
    # Convert the input strings to digits
    a_digits = [int(digit) for digit in a_str]
    b_digits = [int(digit) for digit in b_str]
    # Create a list to store the unit digits of the product
    unit_digits = []
    # Multiply the digits of the first number by the corresponding digit of the second number
    for i in range(len(a_digits)):
        for j in range(len(b_digits)):
            if i + j == len(a_digits):
                # If the last digit of the first number is zero, add the unit digits of the second number
                if a_digits[i] == '0':
                    unit_digits.append(b_digits[j])
                else:
                    # Otherwise, add the two digits and store the result in the unit_digits list
                    unit_digits.append(a_digits[i] * b_digits[j])
            else:
                # If the last digit of the first number is not zero, add the unit digits of the second number
                if a_digits[i] == '0':
                    unit_digits.append(b_digits[j])
                else:
                    # Otherwise, add the two digits and store the result in the unit_digits list
                    unit_digits.append(a_digits[i] * b_digits[j])
    # Convert the unit_digits list to an integer
    product = sum([unit_digits.pop(0) for _ in unit_digits])
    return product


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Set the lower and upper bounds of the range
    lower = a
    upper = b
    
    # Find the largest digit in the range
    largest = 0
    for i in range(a, upper + 1):
        digit = str(i)[-1]
        if digit > largest:
            largest = digit
    
    # Loop through the range and return the even digits
    digits = []
    for i in range(lower, upper + 1):
        digit = str(i)[-1]
        if digit == largest:
            digits.append(digit)
        else:
            digits.append(digit // 2)
    return digits

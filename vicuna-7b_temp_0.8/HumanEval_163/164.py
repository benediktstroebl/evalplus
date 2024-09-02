
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Convert a and b to strings, so that we can compare them as strings
    a_str = str(a)
    b_str = str(b)

    # Find the first non-repeating digit in a_str
    last_digit = a_str[-1] if a_str.isdigit() else 0
    while last_digit in a_str[:-1]:
        last_digit = a_str[-1]

    # Initialize a list to store the even digits
    digits = [0] * (max(a_str, b_str) + 1)
    for i in range(max(a_str, b_str) + 1):
        digits[i] = str(i)

    # Find the first non-repeating digit in b_str
    last_digit = b_str[-1] if b_str.isdigit() else 0
    while last_digit in b_str[:-1]:
        last_digit = b_str[-1]

    # Insert the digits of b_str between a_str digits with the last digit
    # of b_str as the first digit of a_str, so that we get the even digits
    # between a_str and b_str
    for i in range(max(a_str, b_str) + 1):
        if b_str[0] == last_digit:
            digits[i] = digits[i - 1] + str(i)
        else:
            digits[i] = str(i)

    return digits[:-1]
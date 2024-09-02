
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Check for valid input
    if a <= 0 or b <= 0 or a > b:
        return []

    # Generate an empty list to store the even digits
    even_digits = []

    # Iterate through all the numbers between a and b, checking if each digit
    # is even
    for num in range(a, b + 1):
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_digits.append(int(digit))

    # Sort the even digits in ascending order and return the result
    return sorted(even_digits)


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    digits = []
    while b > a:
        digits.append((a, 0))
        a += 1
    digits.append((a, 1))
    while b > a:
        # Find the last digit of the sum of the digits of a and b
        last_digit = a[-1] + b[-1]
        # If the last digit is even, increment the second element of the
        # digit tuple and subtract 1 from both a and b
        if last_digit % 2 == 0:
            digits[-1] = (a[-1], 2 * digits[-1][1] - 1)
            a, b = b - a, a - b
        # Otherwise, add the last digit to the list of digits and update
        # a and b
        else:
            digits.append((a[-1], 1))
            a += 1
            b -= 1
    return digits

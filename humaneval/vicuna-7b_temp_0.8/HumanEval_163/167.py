
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Find the smallest odd number greater than a
    odd = a + (a % 7) + (a % 7 * 13) + (a % 7 * 13 * 13) + (a % 7 * 13 * 13 * 13)
    # Find the smallest multiple of 7 greater than b
    multiple = b // 7
    # Calculate the even digits by combining the appropriate combination of the
    # odd numbers and multiples of 7
    digits = []
    for i in range(1, 8):
        digit = odd // i
        multiple_of_7 = multiple // 7 * i
        digits.append(str(digit) + str(multiple_of_7).zfill(2))
    return digits

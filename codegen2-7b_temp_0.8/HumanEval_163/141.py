
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a < 1 or b < 1:
        return []

    even_digits = []
    current_number = a
    while current_number <= b:
        if current_number % 2 == 0:
            even_digits.append(current_number)
        current_number += 1

    return even_digits


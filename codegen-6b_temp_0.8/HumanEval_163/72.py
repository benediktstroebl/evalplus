
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        return []

    def is_even(number):
        return number % 2 == 0

    def is_digit(number):
        return (number >= 48 and number <= 57)

    stack = []
    for number in range(a, b + 1):
        if is_digit(number):
            stack.append(number)

    return [number for number in stack if is_even(number)]

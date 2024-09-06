
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def is_even(num):
        if num < 2:
            return False
        return True
    digits = []
    while a <= b:
        num = a
        digits.append(num % 2)
        a = a + 1
    return digits

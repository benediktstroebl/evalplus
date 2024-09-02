
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    def is_even_digit(num):
        num = str(num)
        return all(int(char) % 2 == 0 for char in num)

    return sorted(num for num in range(a, b + 1) if is_even_digit(num))


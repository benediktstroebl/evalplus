
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
        return generate_integers(b, a)

    numbers = range(a, b + 1)
    even_numbers = filter(lambda n: n % 2 == 0, numbers)
    return list(even_numbers)

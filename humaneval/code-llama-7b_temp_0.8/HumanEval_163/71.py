
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # FIXME: This could probably be more clever.

    assert a > 0 and b > 0 and a < b

    # We're going to make b larger than a
    if b < a:
        a, b = b, a

    all_integers = range(a, b + 1)

    even_integers = []

    for integer in all_integers:
        integer_str = str(integer)
        for digit in integer_str:
            if int(digit) % 2 == 0:
                even_integers.append(integer)

    return even_integers


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_digits = [str(i) for i in range(a, b + 1)
                   if len(str(i)) == 2 and int(str(i)[1]) % 2 == 0]
    return sorted(list(set(even_digits)))


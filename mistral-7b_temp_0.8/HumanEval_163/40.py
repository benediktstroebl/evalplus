
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def even_digits(x):
        return [i for i in str(x) if i.isdigit() and int(i) % 2 == 0]

    return [int(''.join(even_digits(x))) for x in range(a, b+1) if even_digits(x)]



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    """
    i = a
    while i <= b:
        print(i)
        i += 2
    """
    while a <= b:
        if a % 2 == 0:
            yield a
        a += 1

    print(i)

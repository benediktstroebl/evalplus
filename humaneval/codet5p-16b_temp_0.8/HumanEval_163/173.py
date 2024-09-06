
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # make sure a and b are integers
    a = int(a)
    b = int(b)

    integers = []

    while a <= b:
        str_a = str(a)
        if '0' in str_a:
            a += 1
            continue
        if '4' in str_a or '6' in str_a or '8' in str_a:
            a += 1
            continue

        integers.append(a)
        a += 1

    return integers


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    integers = []

    if a % 2!= 0 or b % 2!= 0:
        return integers

    if a >= b:
        return integers

    if a < b:
        if a % 2 == 0:
            integers.append(a)
        if b % 2 == 0:
            integers.append(b)

    a_next = a + 2
    b_next = b + 2

    while a_next <= b_next:
        integers.append(a_next)
        a_next += 2

    return integers


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    even_ints = []

    for i in range(a, b + 1):
        # If number is even, append to list
        if i % 2 == 0:
            even_ints.append(i)

    return even_ints


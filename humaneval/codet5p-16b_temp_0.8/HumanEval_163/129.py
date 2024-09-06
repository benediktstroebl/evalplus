
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
    a = str(a)
    b = str(b)
    for i in range(int(a[0]), int(b[0]) + 1):
        if int(i) % 2 == 0 and i!= '0':
            integers.append(i)
    return integers

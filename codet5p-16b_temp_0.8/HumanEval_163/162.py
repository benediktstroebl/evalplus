
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    a = str(a)
    b = str(b)
    x = []
    for x in range(int(a), int(b)+1):
        if str(x)[-1] in ['0', '2', '4', '6', '8']:
            x.append(str(x))
    return x

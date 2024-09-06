
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
    if len(a) == len(b):
        return [int(i) for i in a if int(i) % 2 == 0]
    else:
        return [int(i) for i in a[::-1] if int(i) % 2 == 0] + [
            int(j) for j in b if int(j) % 2 == 0
        ]

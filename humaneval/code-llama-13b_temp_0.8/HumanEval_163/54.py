
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    out = []
    for i in range(min(a, b), max(a, b) + 1):
        s = str(i)
        if len(s) > 1 and int(s[1]) % 2 == 0:
            out.append(int(s[1]))
    return out


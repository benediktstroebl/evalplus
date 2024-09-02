
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    while b > a:
        part = [int(x) for x in str(a) if x.is_even]
        a = a + 1
        result.append(part)
    result.append([int(x) for x in str(b) if x.is_even])
    return result

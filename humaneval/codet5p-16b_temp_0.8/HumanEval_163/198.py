
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    assert a >= 0 and b > a
    assert (a % 2 == 0 or a % 10 == 0) and (b % 2 == 0 or b % 10 == 0)
    result = []
    if b % 10 == 0:
        result.extend([a])
    else:
        for i in range(a, b + 1):
            if i % 10 == 0:
                continue
            if i % 2 == 0:
                result.append(i)
    return result


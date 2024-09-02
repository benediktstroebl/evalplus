
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    assert a < b
    if a < 10:
        return list(range(a, b+1))
    elif a == 10:
        return [10]
    else:
        return generate_integers(10, a-1) + generate_integers(a+1, b)

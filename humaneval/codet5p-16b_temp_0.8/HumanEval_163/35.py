
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    assert isinstance(a, int) and isinstance(b, int)
    assert a >= 0 and b >= 0
    assert a <= 2**31 and b <= 2**31

    a_even = a
    b_even = b
    result = []

    while a_even!= 0 and a_even < b:
        if a_even % 2 == 0:
            result.append(a_even)
        a_even += 1

    while b_even!= 0 and b_even < a:
        if b_even % 2 == 0:
            result.append(b_even)
        b_even -= 1

    return result


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Set initially empty result and counter to 0
    res = []
    c = 0
    # Iterate from 2 to b,
    # every time adding 2 to the counter
    while a < b:
        res.append(a + c)
        c += 2
    return res

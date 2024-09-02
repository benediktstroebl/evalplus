
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # convert to string and back to int to ensure the output is
    # not truncated by the float conversion
    return sorted([int(s) for s in str(a) if int(s) % 2 == 0 and int(s) >= a and int(s) <= b])

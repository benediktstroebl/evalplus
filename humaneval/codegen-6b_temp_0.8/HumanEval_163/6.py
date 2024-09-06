
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # replace this for solution
    if(b < a):
        raise ValueError("b is less than a")
    return [x for x in range(a, b+1) if x%2 == 0]



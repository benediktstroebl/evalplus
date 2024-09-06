
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    return [
        i for i in range(a, b + 1)
        if '0' not in str(i) and '1' not in str(i)
        and '2' not in str(i) and '3' not in str(i)
        and '4' not in str(i) and '5' not in str(i)
        and '6' not in str(i) and '7' not in str(i)
    ]

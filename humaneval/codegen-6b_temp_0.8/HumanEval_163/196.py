
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if not is_valid_parameters(a, b):
        return []
    else:
        return sorted([x for x in range(a, b + 1) if all(x % i == 0 for i in range(2, 10))])


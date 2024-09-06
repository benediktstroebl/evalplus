
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a == b:
        return []
    min_val, max_val = sorted([a, b])
    return [n for n in range(min_val, max_val + 1) if n % 2 == 0]


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a >= b:
        return []
    result = [int(d) for d in str(a) if d.is_even()]
    for i in range(b-a-1, -1, -1):
        result.append(a+i)
    result.extend([a+i for i in range(b-a-1, -1, -1)])
    return result

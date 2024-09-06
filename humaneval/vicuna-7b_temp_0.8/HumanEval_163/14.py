
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Handle the edge cases
    if a >= b:
        return []
    elif b >= a + 10:
        return [str(a)]
    else:
        result = [str(a)]
        while b >= a:
            a, b = b, a + 1
            result.append(str(a))
        result.append(str(b))
        return result

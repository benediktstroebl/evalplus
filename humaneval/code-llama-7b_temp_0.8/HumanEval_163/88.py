
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    result = []
    min_value = min(a, b)
    max_value = max(a, b)

    for i in range(min_value, max_value + 1, 2):
        if i % 2 == 0:
            result.append(i)

    return result



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    if a < 1 or b < 1:
        return []
    if a > b:
        return generate_integers(b, a)

    # We need to go up to the end, but not including
    end = b + 1
    result = []

    for i in range(a, end):
        if i % 2 != 0:
            continue
        result.append(i)

    return result


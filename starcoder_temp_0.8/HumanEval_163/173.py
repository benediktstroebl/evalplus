
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    if a > b:
        return []
    a = str(a)
    b = str(b)
    result = []
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            result.append(a[i])
    return result



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b-a+1 not in [2, 3, 4, 5, 6, 7, 8, 9]:
        return []
    result = []
    for i in range(a, b+1, 2):
        if i % 2 == 0:
            result.append(i)
    return result

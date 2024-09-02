
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
    if b > 9:
        return []
    if b < 2:
        return []
    if a < 0:
        return []
    if a < 2:
        a = 2
    if b < 2:
        b = 2
    if b < a:
        return []
    array = []
    for i in range(a, b):
        if i % 2 == 0:
            array.append(i)
    return array



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    array = []
    i = 2
    while i <= b:
        if i % 2 == 0:
            array.append(i)
        i += 1
    return array[a-2:b]


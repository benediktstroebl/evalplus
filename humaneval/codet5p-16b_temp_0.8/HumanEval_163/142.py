
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    list1 = []
    a = int(a)
    b = int(b)
    for i in range(a, b+1):
        if i%2 == 0:
            list1.append(i)
    return list1


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # TODO: Implement this function
    list1 = []
    if a > b:
        temp = a
        a = b
        b = temp
    while a <= b:
        if a % 2 == 0:
            list1.append(a)
            a += 1
    return list1


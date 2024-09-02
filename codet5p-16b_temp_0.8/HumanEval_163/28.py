
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    lst = []
    if b < a or a % 2!= 0: # first check for correct input
        return []
    else:
        if a % 2 == 0: # if a is even, start from a
            lst = [a]
            a += 1
        else: # if a is odd, start from a+1
            lst = [a+1]
            a += 2

    while a <= b:
        if a % 2 == 0:
            lst.append(a)
            a += 1
        else:
            lst.append(a)
            a += 2
    return lst

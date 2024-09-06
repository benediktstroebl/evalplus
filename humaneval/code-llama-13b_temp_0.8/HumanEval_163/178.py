
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
    for x in range(a, b + 1):
        s = str(x)
        for y in s:
            if int(y) % 2 == 0:
                lst.append(int(y))
            else:
                continue
    lst = list(set(lst))
    lst.sort()
    return lst


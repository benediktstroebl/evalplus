
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
    if a%2!= 0 or b%2!= 0:
        return None
    else:
        for i in range(min(a,b), max(a,b), 2):
            lst.append(i)
        return sorted(lst)

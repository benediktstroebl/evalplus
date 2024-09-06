
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # if a is greater than b, reverse them
    if a > b:
        a, b = b, a

    # generate integers between a and b, inclusive
    integers = []
    for i in range(a, b+1):
        integers.append(i)

    # filter integers that have only even digits
    even_integers = []
    for i in integers:
        even = True
        for j in str(i):
            if int(j) % 2 != 0:
                even = False
        if even:
            even_integers.append(i)

    # return sorted integers
    return sorted(even_integers)

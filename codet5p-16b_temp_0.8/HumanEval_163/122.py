
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    result = []
    if a%2 == 1 and b%2 == 1:
        return result
    elif a%2 == 0 and b%2 == 0:
        return result

    elif a%2 == 1 and b%2 == 0:
        for i in range(a, b+1):
            if i%2 == 0:
                result.append(i)
    elif a%2 == 0 and b%2 == 1:
        for i in range(a, b+1):
            if i%2 == 1:
                result.append(i)

    return result

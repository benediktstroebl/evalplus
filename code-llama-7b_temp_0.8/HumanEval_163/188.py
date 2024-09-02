
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
    for i in range(a, b+1):
        if str(i)[0] != '8' and str(i)[1] != '8' and str(i)[2] != '8' and str(i)[3] != '8':
            if i%2 == 0:
                result.append(i)
    return result



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    i, j = 0, 0
    result = []
    while j <= b:
        while i <= a and str(int(a))[i] == '0':
            i += 1
        result.append(a)
        a += 1
        j += 1
    result.extend(str(int(a))[j:].split(''))
    result.reverse()
    return result

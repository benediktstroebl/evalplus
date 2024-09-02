
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
    for number in range(a, b + 1):
        if len(str(number)) % 2:
            continue
        else:
            result.append(int(str(number)[len(str(number)) // 2]))
    return result


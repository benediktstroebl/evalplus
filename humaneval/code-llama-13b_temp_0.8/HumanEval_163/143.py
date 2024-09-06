
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
    for num in range(a, b + 1):
        num = str(num)
        for i in range(len(num)):
            if int(num[i]) % 2 != 0:
                break
        else:
            result.append(int(num))
    return result


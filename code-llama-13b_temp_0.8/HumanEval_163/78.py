
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # left = max(a, b)
    # right = min(a, b)
    # result = []
    # i = left
    # while i <= right:
    #     string_i = str(i)
    #     for digit in string_i:
    #         if int(digit) % 2 == 0:
    #             result.append(int(digit))
    #     i += 1
    # return result

    left = max(a, b)
    right = min(a, b)
    result = []
    i = left
    while i <= right:
        string_i = str(i)
        for digit in string_i:
            if int(digit) % 2 == 0:
                result.append(int(digit))
        i += 1
    return sorted(result)

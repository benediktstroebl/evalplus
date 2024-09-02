
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # # 8kyu
    return sorted([x for x in range(a, b+1) if str(x)[::-1][0] == '0' and x % 2 == 0])

    # # 8kyu
    # return sorted([x for x in range(a, b+1) if x % 2 == 0 and str(x)[::-1][0] == '0'])


    # # 8kyu
    # if a > b:
    #     return generate_integers(b, a)
    # return sorted(set(filter(lambda x: x % 2 == 0 and str(x)[::-1][0] == '0', range(a, b+1))))


    # # 8kyu
    # return sorted(set(filter(lambda x: str(x)[::-1][0] == '0' and x % 2 == 0, range(a, b+1))))



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # a = min(a, b)
    # b = max(a, b)

    # This is an example solution
    # even_integers = []
    # for i in range(a, b + 1):
    #     if str(i)[-1] == '0' and str(i)[-2] == '0':
    #         even_integers.append(i)

    # return even_integers

    # but the following will also work
    return [i for i in range(a, b + 1) if str(i)[-1] == '0' and str(i)[-2] == '0']


def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # (soln 1)
    # evens = []
    # for n in range(a, b + 1):
    #     if n % 2 == 0:
    #         evens.append(n)
    #
    # return evens

    # (soln 2)
    # return [n for n in range(a, b + 1) if n % 2 == 0]

    # (soln 3)
    return [n for n in range(a, b + 1) if n % 2 == 0 and n < 10]


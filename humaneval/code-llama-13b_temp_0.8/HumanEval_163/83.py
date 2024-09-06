
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # YOUR CODE HERE
    result = []
    for i in range(a, b + 1):
        if str(i)[-1] == '0' or str(i)[-1] == '2' or str(i)[-1] == '4' or str(i)[-1] == '6' or str(i)[-1] == '8':
            result.append(i)
    return result



def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # add 1 to the absolute values of a and b so that the loop terminates
    a, b = max(a + 1, b + 1, a + b)

    # initialize the result list
    result = []

    # loop over the range from a to b
    for i in range(a, b + 1):
        # get the string representation of the integer
        str_i = str(i)

        # replace all non-even digits with a placeholder symbol
        placeholder = '?'
        if not str_i.startswith(str(i // 2)):
            str_i = str_i.lstrip('0') + str(placeholder) + str(placeholder)

        # append the resulting string to the result list
        result.append(str_i)

    return result

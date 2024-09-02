
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # create a list
    evens = []
    # for number in range a to b
    for number in range(a, b + 1):
        # check if number is even
        if number % 2 == 0:
            # add number to list
            evens.append(number)
    # return list of evens
    return evens


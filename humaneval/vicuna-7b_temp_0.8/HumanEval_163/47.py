
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # check if a is greater than b
    if a > b:
        # swap the values of a and b
        a, b = b, a
    # create a list to store the even digits
    digits = []
    # iterate over the range of integers from a to b
    for i in range(a, b + 1):
        # check if the current integer is even
        if i % 2 == 0:
            # add the current integer to the list of digits
            digits.append(i)
    return digits

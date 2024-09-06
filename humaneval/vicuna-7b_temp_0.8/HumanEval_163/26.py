
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # sort the integers in ascending order
    a, b = sorted((a, b))
    # initialize the list to store the even digits
    digits = []
    # loop through the integers
    while a <= b:
        # find the middle digit
        middle = (a + b) // 2
        # add the middle digit to the list
        digits.append(middle)
        # update a and b
        a = middle + 1
        b = middle
    # add the first and last digits to the list
    digits.append(a)
    digits.append(b)
    # return the list
    return digits

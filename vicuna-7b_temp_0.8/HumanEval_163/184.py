
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # if a is greater than b, the list will be empty, so we need to check that
    if a > b:
        return []

    # get the digits of a in a list
    digits = [int(d) for d in str(a)]

    # sort the digits in ascending order
    digits.sort()

    # create a list to store the even digits
    even_digits = []

    # loop through the digits and append the even ones to the list
    for i in range(len(digits)):
        if digits[i] % 2 == 0:
            even_digits.append(digits[i])

    # return the list of even digits
    return even_digits

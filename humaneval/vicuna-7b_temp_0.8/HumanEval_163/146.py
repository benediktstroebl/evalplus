
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # base case: return an empty list if a <= b
    if a <= b:
        return []

    # middle case: for i = a to (b-1)/2, increment a by 2 and check
    # if the resulting value is odd
    # if it is odd, append it to the list
    # if it is even, append its digits as a list
    # concatenate the resulting lists and append it to the final result
    result = []
    for i in range(a, b, 2):
        if i % 2 == 0:
            digits = generate_digits(i, b)
            result = result + digits
    return result

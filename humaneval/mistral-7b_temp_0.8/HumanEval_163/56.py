
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # check inputs
    if not isinstance(a, int) or a < 1:
        raise ValueError('first input must be a positive integer')
    if not isinstance(b, int) or b < 1:
        raise ValueError('second input must be a positive integer')

    # check if a and b have same parity
    if a % 2 != b % 2:
        raise ValueError('a and b must have the same parity')

    # initialize the result
    result = []

    # iterate over the range of even numbers between a and b
    for i in range(a, b + 1):
        # check if the current number is even
        if i % 2 == 0:
            # append the current number to the result
            result.append(i)

    return result

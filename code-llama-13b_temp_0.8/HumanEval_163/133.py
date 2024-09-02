
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Use the // operator to get just the digits
    a_digits = [int(d) for d in str(a)]
    b_digits = [int(d) for d in str(b)]

    # Put the longer number first
    if len(a_digits) > len(b_digits):
        first = a_digits
        second = b_digits
    else:
        first = b_digits
        second = a_digits

    # Find the starting point
    start = 0
    for i, d in enumerate(first):
        if d != second[i]:
            start = i
            break

    # Now loop through the rest of the digits
    result = []
    for i in range(start, len(first)):
        if first[i] % 2 == 0:
            result.append(first[i])

    # Return the ascending result
    return sorted(result)


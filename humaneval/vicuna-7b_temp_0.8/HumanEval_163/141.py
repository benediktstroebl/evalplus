
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Handle special case where b is greater than a
    if b > a:
        return list(range(a, b))

    # Initialize result list
    result = []

    # Generate even digits while b is less than a
    while b < a:
        result.append(b % 2)
        b += 2

    # Add a and b to the result list
    result.append(a % 2)
    result.append(a)

    return result

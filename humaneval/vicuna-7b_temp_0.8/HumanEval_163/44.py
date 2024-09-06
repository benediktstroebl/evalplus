
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # Convert the input integers to strings, since we need to concatenate them
    a = str(a)
    b = str(b)

    # Initialize the result list with the first digit
    result = [a[0]]

    # Iterate over the digits of a and b, alternating between them
    for i in range(1, len(a)):
        if a[i] >= b:
            # If the current digit of a is greater than the current digit of b,
            # the result list is already complete, so we can return it
            return result
        else:
            # Otherwise, add the current digit of a and b to the result list
            result.append(a[i])
            result.append(b[i])

    # If we have reached the end of both a and b without finding a digit that
    # is greater than the other, we can return an empty list
    return []

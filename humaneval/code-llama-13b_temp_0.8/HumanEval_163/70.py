
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """

    # Create an array to hold the return values
    integers = []

    # Iterate from a to b.
    for i in range(a, b + 1):
        # If the number is even, add it to the return array.
        if i % 2 == 0:
            integers.append(i)

    return integers


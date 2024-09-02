
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    # First we get the smallest number between a and b
    if a > b:
        smallest = b
    else:
        smallest = a
    # Then we get the largest number between a and b
    if a > b:
        largest = a
    else:
        largest = b
    result = []
    while smallest <= largest:
        if smallest % 2 == 0:
            result.append(smallest)
        smallest += 1
    return result

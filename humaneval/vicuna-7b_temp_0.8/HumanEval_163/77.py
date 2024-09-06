
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b > a:
        return []

    # create a list of all integers from a to b (exclusive)
    integers = [i for i in range(a, b + 1)]

    # filter out the odd numbers
    even_numbers = [i for i in integers if i % 2 == 0]

    return sorted(even_numbers)

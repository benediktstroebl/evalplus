
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    evens = []
    for num in range(a, b):
        if str(num).isdigit():
            if (num % 2) == 0:
                evens.append(num)
    evens.sort()
    return evens


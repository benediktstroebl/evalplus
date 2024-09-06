
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if a > b:
        raise ValueError("a cannot be greater than b")

    integers = []
    for number in range(a, b+1):
        if number % 2 == 0:
            integers.append(number)

    return integers


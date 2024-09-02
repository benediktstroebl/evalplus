
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    first, second = (a, b) if a < b else (b, a)
    nums = []
    for i in range(first, second + 1):
        if i % 2 == 0:
            nums.append(i)

    return nums


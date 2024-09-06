
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    res = []
    for num in range(a, b + 1):
        nums = [int(d) for d in str(num)]
        if num % 2 == 0:
            res.extend(nums)
    return sorted(res)

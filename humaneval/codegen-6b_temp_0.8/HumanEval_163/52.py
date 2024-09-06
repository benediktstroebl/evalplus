
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    if b < a:
        raise ValueError('`b` should be greater than or equal to `a`')
    if a < 0 or b < 0:
        raise ValueError('`a` and `b` should be positive')
    if a % 2 == 0:
        raise ValueError('`a` should be odd')
    even_nums = []
    while a < b:
        if a % 2 == 0:
            even_nums.append(a)
        a += 1
    return even_nums


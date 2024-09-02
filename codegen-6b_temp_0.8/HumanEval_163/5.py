
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    r = []

    if a % 2 == 0:
        a += 1

    if a < b:
        count = b - a
    else:
        count = a - b

    def func(x, y):
        if x > y:
            return False

        elif x < y:
            return True

        return x == y

    while count > 0:
        if func(a, b):
            r.append(a)
            count -= 1

        a += 2

    return r


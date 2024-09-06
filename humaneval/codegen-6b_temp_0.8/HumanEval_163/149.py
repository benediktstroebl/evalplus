
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def generator(limit):
        if limit == 0:
            return []
        elif limit > 0:
            return [limit % 11 + 2] + generator(limit / 11)
        else:
            return generator(abs(limit) / 11 + 1)
    return generator(b) if b > a else generator(a)

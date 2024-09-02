
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def traverse(a, b):
        if a > b:
            return
        res.extend(range(a, b+1, 2))
        traverse(a*10+2, b*10)

    res = []
    traverse(a, b)

    return res


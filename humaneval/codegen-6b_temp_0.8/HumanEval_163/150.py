
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
        return []
    if not isinstance(a, int) or not isinstance(b, int):
        return []
    if a <= 0 or b <= 0:
        return []
    if a % 2 == 0:
        a = a - 1
    if b % 2 == 0:
        b = b - 1
    if a == b:
        return [a]
    def generate_num(n):
        if n == 0:
            return
        if n % 2 == 0:
            return [n] + generate_num(n-2)
        else:
            return generate_num(n-2)
    return generate_num(b-a)

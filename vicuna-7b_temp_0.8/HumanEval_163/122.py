
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    def f(n):
        if n == 0:
            return [0]
        if n % 2 == 0:
            return [n % 2] + f(n // 2)
        else:
            return f(n // 2)

    return sum(f(i) for i in range(a, b + 1))
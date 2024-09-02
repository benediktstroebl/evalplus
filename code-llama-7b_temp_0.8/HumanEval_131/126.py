
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def is_odd(n):
        return n % 2 == 1

    def to_digit(n):
        return n % 10

    def product(ns):
        if ns == []:
            return 1
        else:
            return ns[0] * product(ns[1:])

    def digs(n):
        if n == 0:
            return []
        else:
            return digs(n // 10) + [to_digit(n)]

    return product([x for x in digs(n) if is_odd(x)])

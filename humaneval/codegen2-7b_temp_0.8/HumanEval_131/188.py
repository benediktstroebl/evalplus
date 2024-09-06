
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def product(n):
        total = 0
        while n > 0:
            d = n % 10
            total = total + d
            n = int(n / 10)
        return total

    return product(n

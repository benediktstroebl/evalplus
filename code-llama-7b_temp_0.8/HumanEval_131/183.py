
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def odd_or_even(num):
        if num % 2 == 0:
            return 0
        else:
            return num

    s = 0
    while n > 0:
        s = s * 10 + odd_or_even(n % 10)
        n = n // 10

    return s

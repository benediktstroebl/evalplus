
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n % 2 == 0:
        return 0
    else:
        digits = [int(n % 10) for _ in range(n//10)]
        odd_digits = [x for x in digits if x > 0]
        if len(odd_digits) == 0:
            return 0
        else:
            return sum(x*x for x in odd_digits)

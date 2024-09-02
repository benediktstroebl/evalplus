
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def odd_digits(n):
        if n == 0:
            return ""
        if n % 2 == 0:
            return odd_digits(n // 10)
        return str(n % 10) + odd_digits(n // 10)
    
    d = odd_digits(n)
    if len(d) == 0:
        return 0
    else:
        return int(d)


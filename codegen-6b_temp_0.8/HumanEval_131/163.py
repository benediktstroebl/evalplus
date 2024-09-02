
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digit_set = set()
    while n:
        digit_set.add(n % 10)
        n //= 10
    if len(digit_set) == 1:
        return 0
    else:
        return reduce(mul, digit_set)

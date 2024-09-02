
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n < 1:
        raise ValueError
    digits = []
    for digit in str(n):
        digits.append(int(digit))
    if all([d%2==0 for d in digits]):
        return 0
    else:
        return reduce(lambda x,y:x*y, [d for d in digits if d%2!=0])

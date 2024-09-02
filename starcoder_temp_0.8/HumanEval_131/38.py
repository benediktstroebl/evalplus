
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = []
    for d in str(n):
        digits.append(int(d))
    if len(digits) > 0 and sum(digits) % 2 == 0:
        return 0
    else:
        return sum(digits) % 2

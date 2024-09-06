
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = []
    while n > 0:
        if n%10 % 2 == 1:
            num.append(n%10)
        n//=10
    if len(num) == 0:
        return 0
    else:
        return (num[-1]*num[-2]*num[-3])


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    p=1
    if n<0:
        return 0
    elif n<10:
        return n
    else:
        while n>=10:
            d=n%10
            if d%2!=0:
                p=p*d
            n=n//10
        if n%2!=0:
            p=p*n
        return p


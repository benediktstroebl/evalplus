
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n%2==0:
        return 0
    else:
        i=len(str(n))
        x=0
        while i>0:
            if i%2!=0:
                x=x*int(n%(10**i))
            i=i-1
        return x

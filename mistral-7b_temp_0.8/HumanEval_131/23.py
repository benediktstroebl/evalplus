
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n==0:
        return 0
    else:
        s=str(n)
        o=s.find("1")
        if o>-1:
            s=s.replace("1","",o)
        else:
            return 0
        if o>-1:
            s=s.replace("3","",o)
        else:
            return 0
        if o>-1:
            s=s.replace("5","",o)
        else:
            return 0
        if o>-1:
            s=s.replace("7","",o)
        else:
            return 0
        if o>-1:
            s=s.replace("9","",o)
        else:
            return 0
        s=int(s)
        return s

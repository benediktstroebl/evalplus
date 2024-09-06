
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if len(str(n))==1:
        return n
    elif len(str(n))==2:
        if int(str(n)[0])%2==0 and int(str(n)[1])%2==0:
            return 0
        else:
            return int(str(n)[0])*int(str(n)[1])
    else:
        if int(str(n)[0])%2==0 and int(str(n)[1])%2==0 and int(str(n)[2])%2==0:
            return 0
        else:
            return int(str(n)[0])*int(str(n)[1])*int(str(n)[2])

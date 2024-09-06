
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 10:
        return n
    else:
        l = list(str(n))
        s = []
        for i in l:
            if int(i) % 2!= 0:
                s.append(i)
        if s == []:
            return 0
        else:
            return reduce((lambda x, y: int(x) * int(y)), s)


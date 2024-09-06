
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    l=[]
    for i in str(n):
        if int(i)%2==1:
            l.append(int(i))
    return 1 if l==[] else reduce(lambda a,b:a*b,l)


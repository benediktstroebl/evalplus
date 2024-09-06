
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if str(n)[-1]=="0":
        return 0
    for i in str(n)[::-1]:
        if int(i)%2!=0:
            return int(i)*digits(n//10)
        else:
            return 0

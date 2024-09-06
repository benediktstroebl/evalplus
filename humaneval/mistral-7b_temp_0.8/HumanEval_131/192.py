
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    num = str(n)
    odd = []
    for i in range(len(num)):
        if i%2 == 0:
            odd.append(int(num[i]))
        else:
            odd.append(0)
    return reduce(lambda x,y: x*y, odd)

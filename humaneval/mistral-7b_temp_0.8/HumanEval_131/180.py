
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product=0
    n=str(n)
    for i in range(len(n)):
        if (i%2)!=0:
            product=product*int(n[i])
    return product

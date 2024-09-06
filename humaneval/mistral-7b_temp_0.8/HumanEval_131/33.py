
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    products = 0
    if n==0:
        return products
    if n ==1:
        return n
    n=str(n)
    for i in range(len(n)):
        if int(n[i]) %2 !=0:
            products=int(products)*int(n[i])
        if i == len(n)-1:
            break
    return products



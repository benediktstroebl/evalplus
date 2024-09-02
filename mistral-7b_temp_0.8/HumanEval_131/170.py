
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n=str(n)
    odd_digit=[]
    for i in range(len(n)):
        if n[i]%2!=0:
            odd_digit.append(n[i])
    product=1
    for j in odd_digit:
        product*=int(j)
    return product





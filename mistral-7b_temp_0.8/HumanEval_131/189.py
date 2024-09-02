
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    x = int(n)
    y = []
    while x>0:
        a = x%10
        x = x//10
        if a%2==1:
            y.append(a)
    print(y)
    return 0


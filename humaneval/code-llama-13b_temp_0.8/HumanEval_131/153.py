
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    p = 1
    for n in str(n):
        if int(n) % 2 == 1:
            p *= int(n)
    return p

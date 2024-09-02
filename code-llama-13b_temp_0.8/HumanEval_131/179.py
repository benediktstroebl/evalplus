
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    if n < 10:
        return n
    else:
        s = str(n)
        prod = 1
        for i in s:
            if int(i) % 2 != 0:
                prod *= int(i)
        return prod


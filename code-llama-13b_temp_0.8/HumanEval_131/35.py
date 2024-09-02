
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
        product = 1
        for i in str(n):
            if int(i) % 2 != 0:
                product *= int(i)
        if product == 1:
            return 0
        return product



def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    even = True
    while n > 0:
        modulo = n % 10
        n //= 10
        if modulo % 2 == 0:
            even = False
        else:
            product *= modulo
    return product if even else 0


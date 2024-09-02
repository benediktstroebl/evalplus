
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n > 0:
        product = 1
        for i in range(1, n-1):
            if (n % i) % 2 != 0:
                product *= i
        return product
    else:
        return 0

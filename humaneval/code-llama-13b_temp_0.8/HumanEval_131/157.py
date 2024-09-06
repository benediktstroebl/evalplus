
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
    
    product = 1
    while n > 0:
        n, last_digit = n // 10, n % 10
        if last_digit % 2 != 0:
            product *= last_digit
    return product


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # write your code here
    product = 1
    while n:
        last_digit = n % 10
        if not last_digit % 2:
            n //= 10
        else:
            product *= last_digit
            n //= 10

    return product


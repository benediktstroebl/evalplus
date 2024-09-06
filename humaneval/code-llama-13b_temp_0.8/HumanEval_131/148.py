
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
    number = 1
    while n > 9:
        last_digit = n % 10
        if last_digit % 2 != 0:
            number *= last_digit
        n = n // 10
    return number * n

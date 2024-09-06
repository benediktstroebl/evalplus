
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def is_odd(n):
        return n % 2 == 1

    def digit_of(n):
        return n % 10

    def remove_last_digit(n):
        return n // 10

    product = 1
    while n > 0:
        last_digit = digit_of(n)
        if is_odd(last_digit):
            product *= last_digit
        n = remove_last_digit(n)
    return product


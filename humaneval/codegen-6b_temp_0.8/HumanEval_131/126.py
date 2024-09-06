
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Replace the following line with your code
    last_digit_product = 1
    while n:
        last_digit = n % 10
        if last_digit % 2:
            last_digit_product = last_digit_product * last_digit
        n = n // 10
    return last_digit_product

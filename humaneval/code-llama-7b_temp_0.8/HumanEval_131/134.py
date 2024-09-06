
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    product = 1

    # n = 12345
    # n = 1234
    # n = 123
    # n = 12
    # n = 1

    while n > 0:

        # Get the last digit
        last_digit = n % 10

        # Is it odd?
        if last_digit % 2 == 1:
            product *= last_digit

        # Remove last digit and get the next last digit
        n = int(n / 10)

    return product


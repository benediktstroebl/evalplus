
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    # This is a problem that is best approached by using the modulo operator
    # and looping through the digits of the number.
    # For this approach we first need to figure out how many digits are in the number
    num_digits = len(str(n))

    # Then we need to loop through the number and find the odd digits
    odd_digits = 0
    for i in range(num_digits):
        digit = n % 10
        if digit % 2 == 1:
            odd_digits *= digit
        n //= 10
    return odd_digits

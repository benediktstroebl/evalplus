
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    number = n
    counter = 0
    if number == 0:
        return 0
    while number > 0:
        if number % 10 % 2 != 0:
            counter *= (number % 10)
        number //= 10
    return counter


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    n = str(n)
    evens = 0
    odds = 1
    for char in n:
        if int(char) % 2 == 0:
            evens = evens * int(char)
        else:
            odds = odds * int(char)
    return odds if odds > evens else evens

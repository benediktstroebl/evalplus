
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    odds = 0
    for digit in l:
        if n % digit!= 0:
            odds *= digit
    return

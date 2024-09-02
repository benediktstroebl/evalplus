
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # If the last digit is not 1, then the number of such n-digit positive
    # integers is the same as the number of 10-digit positive integers, since
    # the first digit of the last n-1 digits can be any 10-digit positive
    # integer.
    if n == 0:
        return 10**9
    elif n == 1:
        return 10 + 9*10 + 8*9 + 7*8 + 6*7 + 5*6 + 4*5 + 3*4 + 2*3 + 1*2
    elif n > 10:
        return starts_one_ends(n-1) * 10
    else:
        return 0


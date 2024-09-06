
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def n_digit(n):
        return 10**(n-1)
    def two_one(n):
        return n_digit(n-2) + n_digit(n-1) - 1
    def one_zero(n):
        return (n_digit(n) - 1) + (n_digit(n) - n_digit(n-1))
    def one_one(n):
        return (n_digit(n) - n_digit(n-1)) * 9
    if n <= 2:
        return 0
    if n == 3:
        return two_one(n)
    if n == 4:
        return 0
    if n == 5:
        return two_one(n) + one_zero(n)
    if n == 6:
        return 0
    if n == 7:
        return one_one(n)
    if n == 8:
        return one_zero(n)
    if n == 9:
        return 0
    if n == 10:
        return two_one(n)
    if n == 11:
        return one_one(n)
    if n == 12:
        return one_zero(n)
    if n == 13:
        return 0





def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # you can use modulo to get rid of the leading zeroes
    of_even = (n - (n%10)) / 10
    of_odd = n % 10
    return of_even * of_odd



def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # using a recursive approach with the base case
    # when the number is less than 10, we know that all digits are even
    if n < 10:
        return 0
    # check if all digits are odd
    if sum(str(d) == '1' for d in n) == len(str(n)) % 2 == 0:
        return 0
    # calculate the product of odd digits
    return n // sum(str(d) == '1' for d in n)

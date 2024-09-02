
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # handle the base case of 0 in an optimized way
    if n == 0:
        return 0
    # handle the case where all digits are even
    if sum(n % d == 0 for d in range(10)) == 0:
        return 0
    # handle the other cases by computing the product of the odd digits
    odd_digits = [x for x in range(10) if x % 2 == 1]
    return odd_digits[0] * odd_digits[1] * odd_digits[2] * odd_digits[3] * odd_digits[4]
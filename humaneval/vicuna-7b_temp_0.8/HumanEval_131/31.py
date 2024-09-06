
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # handle base case
    if n < 10:
        return n
    # handle other cases
    if n % 2 != 0:
        return n * digits(n // 2)
    # handle the middle part
    middle = n // 2
    return digits(middle) * digits(n - middle)

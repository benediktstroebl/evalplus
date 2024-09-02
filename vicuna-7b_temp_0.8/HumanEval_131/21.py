
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all digits are even, return 0
    digits = [int(d) for d in str(n)]
    if all(d % 2 == 0 for d in digits):
        return 0

    # Otherwise, use a while loop to keep dividing by 2 until we get an odd digit
    while len(digits) > 0:
        if digits[-1] % 2 != 0:
            # If we get an odd digit, return its product
            return product(digits)
        digits.pop()

    # If we get to the end of the list and there are still even digits,
    # return 0
    return 0

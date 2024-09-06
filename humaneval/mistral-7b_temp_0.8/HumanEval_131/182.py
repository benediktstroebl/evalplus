
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Create a list of all the digits in n.
    digits = [int(d) for d in str(n)]

    # Create a new list of only the odd digits.
    odd_digits = [x for x in digits if x % 2]

    # If the new list is empty, return 0.
    if not odd_digits:
        return 0

    # Multiply all the odd digits together.
    return reduce(lambda x, y: x * y, odd_digits)

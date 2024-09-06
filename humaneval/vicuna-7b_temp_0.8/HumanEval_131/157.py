
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # TODO: Write code to solve this problem
    # ...

    # If all digits are even, return 0
    if all(c % 2 == 0 for c in str(n)):
        return 0

    # Calculate the product of the odd digits
    odd_digits = [x for x in str(n) if x % 2 != 0]
    return reduce(mul, odd_digits, 1)
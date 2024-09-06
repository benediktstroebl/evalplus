
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check for the case where all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0

    # Check for the case where n is 0
    if n == 0:
        return 0

    # Check for the case where n is 1
    if n == 1:
        return n

    # Convert the integer n to a string
    n_str = str(n)

    # Extract the odd digits
    odd_digits = [int(d) for d in n_str if d.isdigit() and d % 2 != 0]

    # If there are no odd digits, return 0
    if len(odd_digits) == 0:
        return 0

    # Otherwise, return the product of the odd digits
    return product(odd_digits)
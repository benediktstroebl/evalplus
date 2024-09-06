
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0
    # Convert n to list of digits
    digits = [int(d) for d in str(n)]
    # Check if n is odd
    if sum(digits) % 2 == 1:
        return sum(map(lambda x: x * (2 ** int(x % 2)), digits))
    # Conversion failed
    return 0


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check for all even case
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0

    # Check for 2^15 case
    if n == 2**15:
        return n

    # Base case
    if n == 1:
        return n

    # Recursive case
    return n * digits(n // 2)

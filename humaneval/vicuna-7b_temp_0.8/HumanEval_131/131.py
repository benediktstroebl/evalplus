
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, n)) == 0:
        return 0

    # Check if last two digits are even
    if n[-2:] == '00':
        # If the last two digits are even, then the odd digits are the first two digits
        return n[:2]

    # If the last two digits are not even, then the odd digits are the odd digits after the first two digits
    odd_digits = n[1:]
    return odd_digits[::-1]
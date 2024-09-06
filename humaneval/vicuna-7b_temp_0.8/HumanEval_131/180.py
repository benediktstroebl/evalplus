
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle the special case of all even digits
    if sum(map(lambda x: x % 2, str(n))) == 0:
        return 0

    # Handle the special case of an odd digit
    if n % 2 != 0:
        return n

    # Otherwise, check the digits in reverse order
    for i in range(len(str(n)) - 1, 0, -1):
        if (n % 10) % 2 != 0:
            return n

    return 0

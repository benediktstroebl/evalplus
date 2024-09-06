
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Handle base case
    if not n % 2:
        return 0

    # Handle the middle case
    if n == 1:
        return n
    d = 1
    for i in range(1, int(n**0.5) + 1):
        d *= n % i
    return d * (n//i)

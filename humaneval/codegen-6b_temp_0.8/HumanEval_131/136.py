
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    total = 1
    # Your code here
    if n < 10:
        total = total * (n % 10)
    elif n % 2:
        for i in range(1, 10):
            total = total * (n % 10)
    else:
        for i in range(1, 10, 2):
            total = total * (n % 10)
    return total

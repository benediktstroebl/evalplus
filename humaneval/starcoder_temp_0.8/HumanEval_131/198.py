
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # base case: zero is trivially divisible by all numbers
    if n == 0:
        return 0
    # if n is odd, then the answer is the product of the remaining digits
    elif n % 2 == 1:
        return n * digits(n//2)
    # if n is even, the answer is the product of the digits after the last 1
    else:
        return digits(n//2)


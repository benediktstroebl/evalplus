
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # First we find the odd digits.
    # This is done by iterating over each digit of n and multiplying the odd digits
    odd_digits = [n%10] if n%2 != 0 else []
    while n > 0:
        n = n//10
        if n%2 != 0:
            odd_digits.append(n%10)
    # We multiply all the odd digits.
    return reduce(lambda x, y: x*y, odd_digits, 1)




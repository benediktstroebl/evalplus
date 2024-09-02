
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a recursive approach
    if n < 10:
        return n
    for i in range(1, n:):
        # If the number is even, return 0
        if n % i == 0:
            return 0
        # If the number is odd, return the product of the odd digits
        else:
            product = n // i
            n = n // 10
            # Recursively call the function again with the remainder
            product = product * digits(n)
            return product
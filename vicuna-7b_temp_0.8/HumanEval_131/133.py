
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a for loop for odd n and a nested for loop for even n
    if n % 2 == 0:
        # Return 0 if all digits are even
        return 0
    else:
        # Calculate the product of the odd digits
        product = 1
        for i in range(1, n // 2 + 1):
            product *= n % i
        return product

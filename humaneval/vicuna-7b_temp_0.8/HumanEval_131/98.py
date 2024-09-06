
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even.
    if sum(map(int, str(n))) % 2 == 0:
        return 0
    # Extract the odd digits.
    digits = [int(d) for d in str(n)]
    # Compute the product.
    product = 1
    for i in range(len(digits) - 1):
        if digits[i] % 2 != 0:
            product *= digits[i]
    return product

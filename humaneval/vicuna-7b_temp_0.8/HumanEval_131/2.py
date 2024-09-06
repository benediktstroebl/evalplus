
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a recursive approach
    # By default, return 0
    if n < 1:
        return 0
    # Calculate the sum of the digits
    # If all digits are even, return 0
    digit_sum = sum(n // i + i * (n % i != 0) for i in range(1, int(n//10) + 1))
    if all(d == 0 for d in digit_sum):
        return 0
    return digit_sum

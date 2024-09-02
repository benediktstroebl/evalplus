
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use an even loop variable to iterate to the end of the string.
    # Use a flag variable to check whether any digit is odd.
    odd_found = 0
    for i in range(len(str(n))):
        if n % 10 == i % 10:
            odd_found += 1
    return odd_found

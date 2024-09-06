
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Using a sliding window to iterate over the digits
    # Store the number of odd digits in the current window
    count = 0
    for i, d in enumerate(n):
        if d % 2 != 0:
            count += 1
    return count


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Get the digit we are checking for
    d = 1
    # Initialize counter
    count = 0
    # Increment counter by 1 for each digit that starts or ends with 1
    for i in range(d, 10 ** (n - 1)):
        if i % 10 == d or i / 10 % 10 == d:
            count += 1
    return count

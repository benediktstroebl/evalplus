
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # First, we check if n is 1. If it is, then we have 1 as the only n-digit
    # number that starts and ends with 1.
    if n == 1:
        return 1
    # Now, we use a for loop to iterate from 1 to n, and check if the number
    # is a 1. If it is, then we increment the count.
    count = 0
    for i in range(1, n+1):
        if str(i) == "1":
            count += 1
    return count

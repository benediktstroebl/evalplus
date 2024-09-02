
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Start by counting the integers that start with 1
    count = 0
    for i in range(1, n):
        count += 10**i

    # Next, count the integers that end with 1
    count += 10**(n-1) * (n-1)

    return count

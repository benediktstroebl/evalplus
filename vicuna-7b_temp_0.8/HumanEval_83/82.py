
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    # iterate and add 1 to the number of times the number is counted
    for i in range(n):
        if (i == n-1 and n % i == 0) or (i == 1 and n % i == 1):
            count += 1
    return count

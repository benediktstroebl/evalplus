
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # count the numbers of n-digit positive integers
    count = 0
    for i in range(1, n+1):
        if str(i).startswith(str(n)) or str(i).endswith(str(n)):
            count += 1
    return count

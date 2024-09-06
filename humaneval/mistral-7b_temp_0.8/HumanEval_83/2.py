
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n = str(n)
    count = 0
    for i in range(1, len(n)):
        count += len(n[0:i] + '1' + n[i:])
    return count




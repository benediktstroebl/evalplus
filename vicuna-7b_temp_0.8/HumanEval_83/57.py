
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n can have at most 1 digit, so we need to check n and n+1 together
    # n+1 can also have at most 1 digit, so we need to check n+2 and n+3 together
    # and so on
    if n % 2 == 0:
        return 0
    count = 0
    for i in range(3, n+1, 2):
        count += len(str(i))
    return count

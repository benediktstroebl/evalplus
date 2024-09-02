
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(n+1):
        if n % i == 0:
            if str(n)[:i] == str(n)[:-i]:
                count += 1
    return count

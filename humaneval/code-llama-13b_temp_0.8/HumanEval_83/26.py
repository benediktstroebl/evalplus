
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, n+1):
        a = str(i)
        if len(a) == n:
            if a[0] == "1" or a[-1] == "1":
                count += 1
    return count


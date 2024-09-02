
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    cnt = 0
    for i in range(1, n + 1):
        start = str(i)[:1]
        end = str(i)[-1:]
        if start == "1" or end == "1":
            cnt += 1
    return cnt


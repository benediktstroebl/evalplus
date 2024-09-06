
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    cnt = 0
    for i in range(n):
        if i > 0 and (i == 1 or i == n):
            cnt += 1
        else:
            for j in range(1, 10):
                cnt += starts_ends(i, j)
    return cnt


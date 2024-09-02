
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n = str(n)
    cnt = 0
    for i in range(1, len(n)+1):
        if n[0] == '1':
            cnt += 1
        elif n[-1] == '1':
            cnt += 1
    return cnt

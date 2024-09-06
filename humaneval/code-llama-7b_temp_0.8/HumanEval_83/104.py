
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    cnt = 0
    # 10^n-1
    end = 10**(n-1) - 1
    # 10^n-n
    start = 10**(n-1) - n
    for i in range(start, end):
        if str(i).startswith("1") or str(i).endswith("1"):
            cnt += 1
    return cnt

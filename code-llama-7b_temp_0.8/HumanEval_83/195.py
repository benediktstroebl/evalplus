
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    l = len(str(n))
    cnt = 0

    for i in range(10**(l-1), 10**l):
        str_i = str(i)
        if str_i.startswith("1") or str_i.endswith("1"):
            cnt += 1
    return cnt

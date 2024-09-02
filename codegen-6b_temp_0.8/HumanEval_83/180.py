
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    d = {str(i): 0 for i in range(10)}
    d[""] = 10
    d[0] = 1
    res = 0
    for i in range(2, n+1):
        for j in range(1, 10):
            if j not in d:
                d[j] = d["1"+str(j)] + d[""+str(j)]
            res += d[str(j)] + d[""+str(j)]
    return res



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    i = 0
    j = 0
    m = 0
    while i < n:
        j = 0
        while j < n:
            if (i==0 or i==n-1) and (j==0 or j==n-1):
                m = m + 1
            j = j + 1
        i = i + 1
    return m

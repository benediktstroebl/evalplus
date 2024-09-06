
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    s = "1"
    i = 1
    count = 0
    while len(s) < n:
        i += 1
        s = s + str(i)
    return s.count("1")


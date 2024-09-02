
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # return (len(str(i for i in range(1,n) if str(i).startswith("1") or str(i).endswith("1"))))
    return len([i for i in range(1, n) if str(i).startswith("1") or str(i).endswith("1")])


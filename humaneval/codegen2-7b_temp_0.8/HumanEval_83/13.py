
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    for i in range(1, 9):
        for j in range(1, 10):
            if str(j)[:n] == str(i)[n - 1:] or str(i)[:n] == str(j)[n - 1:

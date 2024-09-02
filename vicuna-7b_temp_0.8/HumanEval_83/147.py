
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # To count the number of 1-digit numbers
    count = n + 1
    for i in range(2, n+1):
        count = count * (n//i) * (i//1)
    # To count the number of 2-digit numbers
    count = 2 * count
    for i in range(3, n+1):
        count = count * (n//i)
    return count

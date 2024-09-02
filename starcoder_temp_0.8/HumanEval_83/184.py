
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1, 10, 11,..., 1000, 1001,...
    count = 0
    for i in range(1, n + 1):
        count += i
    return count


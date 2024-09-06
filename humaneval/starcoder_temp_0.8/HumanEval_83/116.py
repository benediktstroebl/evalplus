
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, n + 1):
        count += len(str(i)) * 9
        if i % 10 == 1:
            count -= 9
    return count

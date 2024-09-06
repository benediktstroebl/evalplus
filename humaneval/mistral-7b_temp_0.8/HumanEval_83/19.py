
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                count += 1
            elif i == 0 or j == 0:
                count += 9 * (n - 1 - i) * (n - 1 - j)
            else:
                count += 9 * (n - 1 - i) * (n - 1 - j)
    return count

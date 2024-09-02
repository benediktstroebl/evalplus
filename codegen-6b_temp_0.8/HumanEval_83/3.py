
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(n):
        for j in range(10):
            if str(j) + '1' == str(i)[:n] or str(j) + '1' == str(i)[-n:] or '1' + str(j) == str(i)[:n] or '1' + str(j) == str(i)[-n:]:
                count += 1
    return count

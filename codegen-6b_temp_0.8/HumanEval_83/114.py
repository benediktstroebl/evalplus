
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = [1]
    for i in range(2, n + 1):
        count.append(
            count[-1] +
            (count[-1] - 1 if int(str(i)[0]) in [1, 9] else count[-1])
        )
    return count[-1]

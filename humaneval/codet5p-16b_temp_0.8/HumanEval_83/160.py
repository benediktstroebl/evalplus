
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(1, n+1):
        if i % 10 == 1:
            if (i // 10) % 10 == 1 or i == 1:
                count += 1
            elif i < 10:
                continue
            else:
                count += 9 * (i // 10)
        elif i % 10 == 0:
            count += 9 * (i // 10)
        else:
            count += 9 * (i // 10) + (i % 10)
    return count

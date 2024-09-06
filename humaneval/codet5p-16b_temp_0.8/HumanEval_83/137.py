
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    digits = len(str(n))
    count = 0
    for i in range(1, n + 1):
        if i == 1 or i == 10 ** (digits - 1) + 1:
            count += 1
        elif i % (10 ** (digits - 1)) == 1:
            count += 10 ** (digits - 1)
        else:
            count += (10 ** (digits - 1)) * (i % (10 ** (digits - 1)))
    return count

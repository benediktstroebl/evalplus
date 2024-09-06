
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0

    count = 0
    for i in range(1, 10 ** n):
        s = str(i)

        if s[0] == '1':
            count += 1
        if s[-1] == '1':
            count += 1

    return count


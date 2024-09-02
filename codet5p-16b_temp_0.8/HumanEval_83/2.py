
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if not n:
        return 0

    count = 0
    for i in range(1, 10 ** n):
        i = str(i)
        if i[0] == '1' or i[-1] == '1':
            count += 1
    return count

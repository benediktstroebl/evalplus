
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for x in range(1, 10 ** n):
        if str(x)[0] == '1' or str(x)[-1] == '1':
            count += 1
    return count


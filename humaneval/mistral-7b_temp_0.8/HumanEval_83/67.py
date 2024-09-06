
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n == 0:
        return 1
    else:
        for i in range(10 ** (n-1), 10 ** n):
            if str(i)[0] == '1':
                count += 1
        return count


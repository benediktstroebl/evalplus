
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(100, 999):
        x = str(i)
        if x[0] == '1' and x[-1] == '1':
            count += 1
    return

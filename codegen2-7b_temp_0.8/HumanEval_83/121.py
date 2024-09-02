
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 10 ** n):
        if int(str(i)[0]) == 1 or int(str(i)[-1]) == 1:
            count += 1
    return

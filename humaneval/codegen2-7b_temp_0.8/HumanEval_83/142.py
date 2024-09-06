
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for x in range(10):
        num = [int(i) for i in str(x)]
        if x in num:
            count += 1
    return

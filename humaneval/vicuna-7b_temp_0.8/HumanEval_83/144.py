
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # for i in range(n+1, max(n, 1000000)):
    for i in range(1, max(n+1, 1000000)):
        count = 0
        for d in range(i):
            if d % 2 == 1:
                count += 1
        if count > 0:
            yield i, count

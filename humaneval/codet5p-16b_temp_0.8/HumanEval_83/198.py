
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    counter = 0
    for i in range(1, n+1):
        if i % 10 == 1 or i // 10 == 1:
            counter += 1
    return counter

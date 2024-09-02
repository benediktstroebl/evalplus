
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 10 ** n):
        if i == 1:
            count += 1
        if i % 10 == 1:
            count += 1
        if i % 100 / 10 == 1:
            count += 1
        if i / 1000 == 1:
            count += 1
        if i / 10000 == 1:
            count += 1
        if i / 100000 == 1:
            count += 1
        if i / 1000000 == 1:
            count += 1
    return count


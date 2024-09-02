
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    if n == 2:
        return 10

    max_number = 10 ** (n - 1)
    min_number = 10 ** (n - 2)
    count = 0
    for i in range(min_number, max_number + 1):
        if i % 10 == 1 or i % 10 == 9:
            count += 1
        if i % 100 == 10 or i % 100 == 99:
            count += 1

    return count


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, n):
        if i < 10:
            count += 2
        elif i % 10 == 1 or i % 100 == 1:
            count += 1
    if n < 10:
        count += 2
    elif n % 10 == 1 or n % 100 == 1:
        count += 1
    return count


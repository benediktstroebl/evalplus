
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_digits = len(str(n))
    count = 0
    for i in range(0, n_digits+1):
        if i == 0:
            count += 1
        elif i == 1:
            count += 1
        elif i == n_digits:
            count += 1
        else:
            count += 2
    return count

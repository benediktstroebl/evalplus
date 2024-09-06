
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_count = 0
    for i in range(1, n+1):
        if i < 10:
            n_count += 1
        elif i >= 10:
            if ((i/10) % 10 == 1) | ((i/10) % 10 == 0):
                n_count += 1
    return n_count

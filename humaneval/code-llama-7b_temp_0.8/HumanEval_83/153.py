
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    n_range = 10**(n-1)
    for i in range(1, 10**n):
        if i % n_range == 0:
            if str(i)[:1] == '1' or str(i)[-1:] == '1':
                count += 1
    return count

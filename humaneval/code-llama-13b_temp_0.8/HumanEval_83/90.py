
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n==1:
        return 2
    elif n==2:
        return 3
    else:
        n_end_1 = 9
        n_start_1 = 10
        for _ in range(n-2):
            n_end_1 *= 10
            n_start_1 *= 10
        return n_start_1 + n_end_1 - 1


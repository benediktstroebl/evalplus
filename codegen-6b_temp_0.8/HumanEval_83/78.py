
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_digit = len(str(n))
    # Number of different starting digits
    n_start = 0
    for i in range(10**(n_digit - 1), 10**n_digit):
        if str(i)[0] == '1':
            n_start += 1
    # Number of different ending digits
    n_end = 0
    for i in range(10**(n_digit - 1), 10**n_digit):
        if str(i)[-1] == '1':
            n_end += 1
    return n_start * n_end


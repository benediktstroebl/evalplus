
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    if n <= 1:
        return count
    n_s = str(n)
    n_len = len(n_s)
    if n_s[0] == '1' or n_s[-1] == '1':
        count += 1
    for i in range(1, n_len):
        if n_s[:i] == '1' or n_s[i:] == '1':
            count += 1
    return count

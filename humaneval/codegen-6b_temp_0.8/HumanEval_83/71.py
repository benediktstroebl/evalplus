
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    p = 10**(n-1)
    n_s_1 = 0
    n_e_1 = 0

    for i in range(p, 10**(n+1)):
        s, e = str(i), str(i)[::-1]
        if s[0] == '1':
            n_s_1 += 1
        if e[0] == '1':
            n_e_1 += 1

    return n_s_1, n_e_1


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n_str = str(n)
    return sum(1 for pos, ch in enumerate(n_str) if ch == '1' and
               (pos == 0 or n_str[pos - 1] != '1'))


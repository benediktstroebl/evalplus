
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return len([p for p in pandigital_strings(n)
                if p[0] == '1' or p[-1] == '1'])

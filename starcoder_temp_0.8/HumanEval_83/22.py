
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Any number of 1's at the start or end can be represented by the
    # following regex: ^1+|1+$
    return len(re.findall(r'^1+|1+$', str(n)))

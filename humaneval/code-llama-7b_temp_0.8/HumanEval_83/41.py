
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_one = end_one = 0
    for i in range(1,10**n):
        if str(i).startswith('1'):
            start_one += 1
        if str(i).endswith('1'):
            end_one += 1
    return start_one + end_one


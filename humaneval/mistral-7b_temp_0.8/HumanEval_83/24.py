
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    number_one = 0
    number_one_ends = 0
    number_one_starts = 0
    for i in range(1, n+1):
        if str(i).startswith('1') or str(i).endswith('1'):
            number_one += 1

    for i in range(1, n+1):
        if str(i).startswith('1') and str(i).endswith('1'):
            number_one_starts += 1

    for i in range(1, n+1):
        if str(i).endswith('1'):
            number_one_ends += 1

    return number_one - number_one_ends - number_one_starts


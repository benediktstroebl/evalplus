
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1, 10**(n-1)):
        str_num = str(i)
        if str_num.startswith('1') or str_num.endswith('1'):
            count += 1
    return count


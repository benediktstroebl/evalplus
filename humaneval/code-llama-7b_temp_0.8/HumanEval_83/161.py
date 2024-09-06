
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count_start = 0
    count_end = 0
    for num in range(1, 10**n):
        str_num = str(num)
        if str_num.startswith('1'):
            count_start += 1
        if str_num.endswith('1'):
            count_end += 1
    return count_start + count_end

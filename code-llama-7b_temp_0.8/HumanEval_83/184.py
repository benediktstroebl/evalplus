
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    num = 1
    while num < 10**n:
        str_num = str(num)
        if str_num[0] == '1' or str_num[len(str_num)-1] == '1':
            count += 1
        num += 1
    return count

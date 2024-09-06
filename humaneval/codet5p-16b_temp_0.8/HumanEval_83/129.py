
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def starts_ends(num):
        num = str(num)
        if len(num) == 1 and num == '1': return 1
        if len(num) == 1: return 0
        if num[0] == '1' and num[-1] == '1': return 1
        else: return 0

    if n == 1: return 0

    count = 0

    for num in range(10**(n-1), 10**n):
        count += starts_ends(num)

    return count

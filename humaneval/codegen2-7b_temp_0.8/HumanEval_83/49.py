
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    nums = []
    for i in range(10**n):
        if str(i)[:1] == '1':
            nums.append(i)
    return len(n

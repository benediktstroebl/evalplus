
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = []
    for num in range(1, 10**n):
        if str(num).startswith('1') or str(num).endswith('1'):
            result.append(num)
    return len(result)




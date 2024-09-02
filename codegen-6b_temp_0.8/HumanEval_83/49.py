
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    for i in range(1, n + 1):
        if i < 10:
            result += 1
        else:
            result += int(str(i).startswith('1') or str(i).endswith('1'))
    return result


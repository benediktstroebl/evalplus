
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    result = 0
    # Check how many numbers in this range start with 1
    for i in range(100, n + 1):
        if int(str(i)[0]) == 1:
            result += 1
    # Check how many numbers in this range end with 1
    for i in range(n - 1, 0, -1):
        if int(str(i)[-1]) == 1:
            result += 1
    return result

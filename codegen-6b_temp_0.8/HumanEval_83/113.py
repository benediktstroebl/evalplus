
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(10):
        count += len(str(i)*n)
    count += 1
    for i in range(10, n+1):
        test_val = 0
        for j in range(10):
            test_val += len(str(j)*i)
        count += test_val
    return count


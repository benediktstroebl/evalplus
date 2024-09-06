
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start = end = 0
    prefix = pow(10, n - 1)
    count = 0
    for i in range(1, pow(10, n)):
        if i % prefix == 1:
            start += 1
        if i % prefix == 0:
            end += 1
            
    return start + end


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start = 0
    end = 0
    for i in range(1, 10**n):
        if i % 10 == 1:
            start += 1
        if i % 10 == 0:
            end += 1
    return start + end

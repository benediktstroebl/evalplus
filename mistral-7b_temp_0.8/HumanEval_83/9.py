
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in range(1, n):
        for j in range(10**(n - i)):
            if str(10**(n - i) + j)[0] == '1':
                total += 1
    return total


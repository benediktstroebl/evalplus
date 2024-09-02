
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    num = 0
    for i in range(n):
        if (n % i == 0 and i not in range(2, n//i+1)) or (n // i == 0 and i not in range(1, n//i-1)):
            num += 1
    return num

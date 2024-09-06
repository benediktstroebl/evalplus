
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1,n+1):
        if n % i == 0 and (i-1) % 10 in [1,9]:
            count += 1
        elif n % i == 0 and i % 10 in [1,9]:
            count += 1
    return count

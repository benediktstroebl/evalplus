
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Add 1 to account for 1 as the first digit
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
        elif n % i == 1:
            count += 2
    return count

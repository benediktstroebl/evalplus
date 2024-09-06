
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    i = 1
    while n > 0:
        if n % i == 0:
            n //= i
            count += 1
        i += 1
    return count

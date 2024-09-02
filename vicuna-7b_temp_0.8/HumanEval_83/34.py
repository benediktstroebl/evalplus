
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Save the number of 1s at the end as "last_one".
    last_one = n % 10
    count = 0
    for i in range(n // 10):
        if n % 100 == 100 - i:
            count += 1
        if n % 100 == 100 - i - 1:
            count += 1
    return count


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for num in range(n):
        if num < 10:
            count += 1
        elif num % 10 == 1 or num // 10 == 1:
            count += 1
    return count


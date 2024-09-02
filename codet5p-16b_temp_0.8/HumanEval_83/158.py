
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    
    count = 0
    for i in range(n):
        num = i + 1
        if num < 10:
            count += 1
        elif num % 10 == 1:
            count += starts_one_ends(n - 1)
        else:
            count += starts_one_ends(n - 1) - starts_one_ends(n - 2)
    return count


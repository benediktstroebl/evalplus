
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    total = 0
    for i in range(1, n):
        # add to total the numbers starting or ending with 1
        if i % 10 == 1:
            total += 10**i
    return total * 2



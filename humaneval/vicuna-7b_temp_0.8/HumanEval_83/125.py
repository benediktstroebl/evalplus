
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # check if n is even or odd
    if n % 2 == 0:
        count = 0
        for i in range(n):
            if i % 2 == 0:
                count += 1
        return count
    else:
        count = 0
        for i in range(n - 1, -1, -1):
            if i % 2 == 0:
                count += 1
        return count

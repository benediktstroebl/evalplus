
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n < 2:
        return 0
    if n < 3:
        return 1
    if n % 10 == 1:
        count = 1
        for i in range(n//10):
            if n % 100 == 1:
                count += 1
        return count
    if n % 10 == 2:
        count = 1
        for i in range(n//10):
            if n % 100 == 2:
                count += 1
        return count
    if n % 10 == 3:
        count = 1
        for i in range(n//10):
            if n % 100 == 3:
                count += 1
        return count
    if n % 10 == 4:
        count = 1
        for i in range(n//10):
            if n % 100 == 4:
                count += 1
        return count
    return 0

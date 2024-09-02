
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if i == 1 or k == 1:
                    count += 1
    return count

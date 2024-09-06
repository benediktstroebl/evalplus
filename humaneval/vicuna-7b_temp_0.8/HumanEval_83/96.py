
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 1:
        return 0
    else:
        result = 0
        for i in range(n):
            for j in range(i, n):
                if (j % 10 == 1 and n % j == 0) or (n % 10 == 1 and n % j == 0 and j > 1):
                    result += 1
        return result

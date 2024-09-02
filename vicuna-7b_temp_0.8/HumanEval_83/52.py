
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 1:
        return 1
    else:
        count = 0
        for i in range(1, n+1):
            if str(i) == '1':
                count += 1
            else:
                count += (n // i) * (n // i - 1) // 2
        return count

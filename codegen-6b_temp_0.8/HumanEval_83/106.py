
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n > 0:
        count = 0
        for a in range(1, n+1):
            s = str(a)
            if s[0] == '1':
                count += 1
            if s[-1] == '1':
                count += 1
        return count
    else:
        return 0

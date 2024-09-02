
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    n += 1
    s = str(n)
    count = (n - 9 * (n // 9)) * (n // 9) + (n - 1) * (n // 9) + 1 if s[0] == '1' or s[-1] == '1' else 0
    for i in range(2, len(s) - 1):
        if s[i - 1] == '1' and s[i]!= '9' and s[i + 1]!= '1':
            count += 1
        if s[i - 2]!= '1' and s[i - 1] == '9' and s[i]!= '1' and s[i + 1]!= '1':
            count += 1
    return count


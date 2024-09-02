
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    n = str(n)
    if n[0] == '1':
        count += 1
    if n[-1] == '1':
        count += 1
    if n.startswith('1') and n.endswith('1'):
        count -= 1
    return count

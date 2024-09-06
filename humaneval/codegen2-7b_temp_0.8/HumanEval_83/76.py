
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    i = 0
    while i * 10 <= n:
        i += 1
        if str(i) * i == str(n):
            print(i)
            return i
    return

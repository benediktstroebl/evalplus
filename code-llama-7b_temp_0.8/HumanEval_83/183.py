
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(map(lambda n: 1 if int(n[0] == '1' or n[-1] == '1') else 0, range(10 ** (n - 1), 10 ** n)))

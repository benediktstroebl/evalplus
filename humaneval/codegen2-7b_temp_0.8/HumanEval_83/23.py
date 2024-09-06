
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(int(n[i]) == 1 or int(n[i]) == 9 for i in range(len(n

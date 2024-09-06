
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1:
        return 1
    elif n % 10 in [1, 9]:
        return 1
    else:
        return (sum(starts_one_ends(n//10)) + sum(starts_one_ends(n//10+1))) % 10

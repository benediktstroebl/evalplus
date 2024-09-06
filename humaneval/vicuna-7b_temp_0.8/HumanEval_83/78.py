
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 1^0=1, 1^1=0, 1^2=0
    if n == 0:
        return 1
    # base case
    if n == 1:
        return 1
    # 2-digit case
    for i in range(2, min(n//2+1, 10)):
        if n % i == 0:
            for j in range(i, min(n//i+1, 10)):
                if n % j == 0:
                    return 1
    return 0

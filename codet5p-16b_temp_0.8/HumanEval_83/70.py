
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0
    for i in range(n+1):
        digits = [int(x) for x in str(i)]
        if digits[0] == 1 or digits[-1] == 1:
            count += 1
    return count

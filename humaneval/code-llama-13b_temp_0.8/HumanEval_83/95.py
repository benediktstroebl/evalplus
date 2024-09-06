
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # return the count of numbers in the range 10 ** (n - 1) <= x <= 10 ** n
    # whose digits starts or ends with 1
    if n < 1:
        return 0
    count = (n - 1) * 2
    for x in range(2, n):
        if x % 2 == 0:
            count += 1
        else:
            count += 2
    return count


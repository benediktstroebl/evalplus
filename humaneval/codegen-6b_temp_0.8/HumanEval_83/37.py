
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    ones = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(10 ** (n - 1)):
        num = str(i)
        if num[0] in ones:
            count += 1
        if num[-1] in ones:
            count += 1
    return count


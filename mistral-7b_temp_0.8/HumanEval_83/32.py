
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    num = str(n)
    if len(num) == 1:
        return 1
    else:
        for i in range(len(num)):
            if int(num[i]) == 1:
                count += 1
        return count


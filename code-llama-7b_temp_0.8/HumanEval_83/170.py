
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    count = 0

    if n > 0 and n < 11:
        count += 1
    elif n > 10:
        for i in range(10):
            if str(i)[0] == "1":
                count += 1
        for i in range(10):
            if str(i)[-1] == "1":
                count += 1

    return count


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0

    for i in range(1, n + 1):
        number = str(i)
        if number[0] == "1":
            count += 1
        elif number[-1] == "1":
            count += 1

    return count

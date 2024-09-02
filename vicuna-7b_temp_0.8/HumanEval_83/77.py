
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if n is 1, return 1
    if n == 1:
        return 1

    # if n is 2, return 1
    if n == 2:
        return 1

    # if n is 3, return 1
    if n == 3:
        return 1

    # if n is 4, return 2
    if n == 4:
        return 2

    # if n is 5, return 2
    if n == 5:
        return 2

    # use a while loop to iterate through the first n digits
    count = 0
    while n > 0:
        # check if the number starts with 1
        if n % 10 == 1:
            count += 1
        # check if the number ends with 1
        if n % 10 == 1 and (n // 10) % 10 == 1:
            count += 1
        # subtract 10 from the number
        n = n // 10

    return count

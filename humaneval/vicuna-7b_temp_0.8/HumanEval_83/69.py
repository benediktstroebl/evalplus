
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # initialize count variable
    count = 0
    # loop through the digits of n
    for i in range(10):
        # check if n starts with 1
        if n[0] == 1:
            count += 1
        # check if n ends with 1
        elif n[-1] == 1:
            count += 1
        # add the current digit to the count
        count += int(n[-2])
    return count


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # make n-1 to avoid division by 0
    n -= 1
    # store the count of n-digit numbers that start with 1
    start1 = 0
    # store the count of n-digit numbers that end with 1
    end1 = 0
    for i in range(2, n):
        # check the digit from 1
        if i % 10 == 1:
            # update the count of n-digit numbers that start with 1
            start1 += 1
        else:
            # update the count of n-digit numbers that end with 1
            end1 += 1
    # return the sum of start1 and end1
    return start1 + end1

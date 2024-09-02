
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # initialize count
    count = 0
    # check numbers with one or more 1s
    for i in range(10**(n-1),10**n):
        # if the number starts or ends with 1, increment count
        if str(i)[0] == "1" or str(i)[-1] == "1":
            count += 1
    # return count
    return count


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    starts_one = 0
    ends_one = 0
    # i is the number of 1s in the first position
    for i in range(n+1):
        if i == 1:
            starts_one += 1
        # i is the number of 1s in the last position
        for j in range(n-i+1):
            if j == n-i:
                ends_one += 1
            else:
                ends_one += 10**(n-i-j)
    return starts_one + ends_one



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # n = 1 is not a valid input, so handle that separately
    if n == 1:
        return 1
    # base case for the recursion
    if n == 2:
        return 1
    # start by adding 1 to the list
    ones = [1]
    # add all the numbers from 2 to n to the list
    for i in range(2, n+1):
        ones.append(i)
        # check if the number ends with 1
        if i % 10 == 1:
            ones.append(i)
    # use the fact that the last digit of n must be 0 (since it starts with 1)
    # to count the number of n-digit positive integers that start with 1
    count = 0
    for x in ones:
        if x > 10:
            # we only count n-digit positive integers
            count += len(str(x)) - 1
    return count

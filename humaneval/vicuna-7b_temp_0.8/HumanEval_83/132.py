
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case
    if n == 1:
        return 1
    # calculate the counts
    counts = [0, 0]
    for i in range(n):
        # for the current digit
        if n % i == 0:
            # start
            counts[i % 2] += 1
        else:
            # end
            counts[(i + 1) % 2] += 1
    return counts

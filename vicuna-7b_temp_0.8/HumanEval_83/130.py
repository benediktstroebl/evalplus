
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # the dictionary contains the counts of n-digit numbers
    counts = {i: 0 for i in range(10)}

    # initialize the count of n-digit numbers starting with 1
    counts['1'] += n // 10

    # initialize the count of n-digit numbers ending with 1
    counts[str(n // 10)] += n % 10 == 1

    # iterate over the remaining digits
    for i in range(10):
        counts['1'] -= counts['1'] % 10 == 1
        counts[str(i)] += 1

    return counts['1'] + counts[str(n // 10)]

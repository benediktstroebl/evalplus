
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # START CODE HERE
    return math.factorial(n + 1) // (math.factorial(n) * math.factorial(n + 1))

    # END CODE HERE

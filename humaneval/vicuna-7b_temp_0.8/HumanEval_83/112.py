
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Create a list of all n-digit positive integers
    nums = [str(x) for x in range(10**n)]
    # Create a list of 1-digit positive integers
    ones = [str(x) for x in range(10)]
    # Count the numbers of n-digit positive integers that start with 1
    ones_starting = [1 if str(x)[-1] == '1' else 0 for x in nums]
    # Count the numbers of n-digit positive integers that end with 1
    ones_ending = [1 if str(x)[0] == '1' else 0 for x in nums]
    # Return the sum of the two counts
    return sum(ones_starting) + sum(ones_ending)

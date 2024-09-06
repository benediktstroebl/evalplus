
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Explanation
    # first we find the number of numbers of n-digit positive integers that end with 1,
    # as n-digit integers that start with 1 is the same as those that end with 1.
    # then we find the number of n-digit positive integers that start with 1
    # then we return the result

    # Initialization
    num_of_nums = 0

    # Condition 1
    if n == 1:
        return 9
    elif n == 2:
        return 18
    else:
        # Condition 2
        num_of_nums_that_end_with_1 = (9 * 10 ** (n - 1)) + (9 * 10 ** (n - 2)) + 1
        num_of_nums_that_start_with_1 = (9 * 10 ** (n - 1))
        # Return
        return num_of_nums_that_end_with_1 + num_of_nums_that_start_with

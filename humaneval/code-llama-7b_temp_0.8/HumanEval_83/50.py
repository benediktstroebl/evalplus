
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 10^(n-1) is max of 1-digit integers
    # 10^n is max of n-digit integers
    # 10^(n-1) - 10 is the range of valid n-digit integers
    # 10^(n-1) - 10 is 1 less than the number of valid n-digit integers
    # The range has 21 choices for each digit (10 options for each digit)
    # This is a one-time calculation and is stored as a variable
    digits = 10**(n-1) - 10
    # The 21 choices are stored in a list for easy access
    choices = [10**(n-1) - 10] + list(range(10, 10**(n-1)))
    # The max number of choices is 10
    # The number of 1-digit integers that start or end with 1 is 9
    # The number of 2-digit integers that start or end with 1 is 81
    # The number of 3-digit integers that start or end with 1 is 729
    # The number of 4-digit integers that start or end with 1 is 6561
    # The number of 5-digit integers that start or end with 1 is 59049
    # The number of 6-digit integers that start or end with 1 is 531441
    # The number of 7-digit integers that start or end with 1 is 4782969
    # The number of 8-digit integers that start or end with 1 is 43046721
    # The number of 9-digit integers that start or end with 1 is 391551625
    # The number of 10-digit integers that start or end with 1 is 3640153313
    # The number of 11-digit integers that start or end with 1 is 33813592625
    # The number of 12-digit integers that start or end with 1 is 3

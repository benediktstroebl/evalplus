
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Your code here
    # What is the first digit of the first number with the first digit 1?
    # 10 - 1 = 9
    # 90 - 1 = 89
    # 890 - 1 = 889
    # ...
    # 990 - 1 = 989
    # 999 - 1 = 989
    #
    # Therefore, if the first digit is 1, the last digit must be between 8 and 9,
    # inclusive.
    # There are 9 of those.
    #
    # The first number with the second digit 1 is 100.
    # The last number is 9999.
    #
    # Therefore, if the second digit is 1, the last digit must be between 8 and 9,
    # inclusive.
    # There are 9 of those.
    #
    # The first number with the third digit 1 is 10000.
    # The last number is 99999.


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Note that it's O(n) to generate all the digits 1 to n
    one_digit_count = 0
    if n == 1:
        one_digit_count = 10
    elif n == 2:
        one_digit_count = 15
    elif n == 3:
        one_digit_count = 25
    else:
        # for n > 3, we use the following algorithm
        # count the number of ways to create a "natural" number of n-1
        # digits, and add 1 to count for each way to create a number
        # of n-1 digits that starts with 1
        start_with_one = starts_one_ends(n - 1)
        # similarly, count the number of ways to create a "natural" number
        # of n-1 digits, and add 1 to count for each way to create a number
        # of n-1 digits that ends with 1
        end_with_one = starts_one_ends(n - 1)
        # now we add to the count by the number of ways to create a "natural"
        # number of n-1 digits that starts with 1 and ends with 1
        one_digit_count = start_with_one + end_with_one
        # subtract the two ways to create a number of n-1 digits ending with 1
        # and the ways to create a number of n-1 digits that starts with 1
        one_digit_count -= end_with_one

    # now we want to count the number of ways to create a positive integer
    # that has n digits.  We start with the base case of 1 digit, and add
    # a way to create a number of n-1 digits that starts with 1, and add a
    # way to create a number of n-1 digits that ends with 1
    # (there are O(n-1) ways to create the number of n-1 digits that starts with 1)
    start_with_one = starts_one_ends(n - 1)
    one_digit_count += start_with_one

    # similarly, we want to count the number of ways to create a positive
    # integer that has n digits.  We start with the base case of n digits,
    # and add
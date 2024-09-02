
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Our base case is that n is 0.
    # This would mean that our number has no digits.
    # In this case, we can return 0.
    if n == 0:
        return 0

    # Now we need to deal with the case when n > 0.
    # Here, we can subtract the numbers that do not start with 1 or end with 1.
    # We can do this by subtracting the results of the recursive calls with
    # a number of digits less than n, where we subtract the number of numbers
    # that start or end with 0 from n.
    # We can get the number of numbers that start or end with 0 by subtracting
    # the number of numbers that start or end with 1 from n.
    # This is easy to get:
    #
    # (number of numbers that start or end with 0) = n - starts_one_ends(n-1)
    #
    # We can do this for both the number of numbers that start with 1 and end
    # with 1.
    # This gives us:
    #
    # (number of numbers that start with 1) = starts_one_ends(n)
    # (number of numbers that end with 1) = ends_one(n)

    return n - starts_one_ends(n - 1) - ends_one(n - 1)


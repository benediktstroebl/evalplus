
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # This is a little bit tricky, but we can do it by breaking down to the
    # cases of adding or deleting a single digit.
    # Here is a breakdown of the cases:
    #   (1)    n > 1: (1, 0)     n - 1 > 0: (1, 0)
    #   +----------------------+-----+
    #   |                 n is odd:
    #   |                     (n - 1) is even: (1, 0)
    #   |                     (n - 1) is odd: (n, 0)
    #   |
    #   +-------------------n is even:
    #   |                    (n - 1) is even: (n, 0)
    #   |                    (n - 1) is odd: (n, 1)
    #
    # The first line above says that n > 1 and n isn't even. If we lift the
    # fact that n is odd, then we can write the input as being an even number.
    # The second line then states that the input is odd. So we can look at the
    # first bit when adding and when removing from the last digit. If the
    # last digit is a 1, then we remove it. If the last digit is a 0, then we
    # add it.
    #
    # We can see from the second line that the input is odd. Thus, we can pick
    # the case where we want to remove a single digit and add a single digit.
    # We also know that we can pick a case where the last digit isn't a 1, so
    # we pick one.
    #
    # From the tip of the iceberg:
    # If we do not select a case where we want to add a 1, we will have
    # duplicates! It is not possible to remove a single digit from an even
    # number. If we remove a single digit, we get one more valid result.
    #
    # The only way to get to the final result is to remove a single digit from
    # the input and add a 1 to it, which can only result in one valid result.
    #
    # If we choose to remove a single digit, we can have duplicates. This is
    # exactly the same as when
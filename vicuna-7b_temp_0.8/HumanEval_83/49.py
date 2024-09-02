
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # the count of n-digit positive integers that start or end with 1
    # n-1 choice for the digit that can be 1, so n-1 choice for the digit
    # that can be 1 and n-1 choice for the digit that can be 1
    # means n-1 choose 1
    # and (n-1 choose 1) choose 1 = n choose 2 = n! / (2! (n-2)!)
    # so the count is n! / (2! (n-2)!)
    # so the count of n-digit positive integers that start or end with 1
    # is n! / (2! (n-2)!)
    # which is 5 for n=5
    # which is 120 for n=6
    # which is 2048 for n=7
    # and so on
    return (n * (n-1) * (n-2)) / 6

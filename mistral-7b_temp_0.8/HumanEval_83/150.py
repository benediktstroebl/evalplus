
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    start_one = 0
    end_one = 0
    if n == 1:
        start_one = 1
        end_one = 1
    else:
        for i in range(1, n):
            start_one += end_one
            end_one += start_one
    return start_one + end_one

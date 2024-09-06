
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # if n == 1:
    #     return 1
    # if n == 2:
    #     return 2
    # return 9*2**(n-3)

    if n == 1:
        return 1
    if n == 2:
        return 2
    return (9*2)**(n-2)

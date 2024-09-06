
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    #count how many 1's are in the first position
    #count how many 1's are in the last position

    if n == 1:
        return 10
    elif n == 2:
        return 45
    else:
        num_1_first = 10 * (10 ** n-1) + 9 * (10 ** n-1)
        num_1_last = 10 * (10 ** n-1) + 9 * (10 ** n-1)

        return num_1_first + num_1_last

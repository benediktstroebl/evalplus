
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def num_of_1_ends(n, s):
        if n == 1:
            return s
        else:
            s += n - 1 - (n - 1) % 2
            return num_of_1_ends(n - 1, s)

    return num_of_1_ends(n, 0)


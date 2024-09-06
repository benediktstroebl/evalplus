
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def digit_count(n, d):
        """
        Given a positive integer n, return the number of n-digit positive
        integers that have digit d in the tens place.
        """
        if n == 1:
            if d == 1:
                return 1
            else:
                return 0
        else:
            return 10 * digit_count(n - 1, d) + (d == 1)

    return digit_count(n, 1) + digit_count(n, 10)


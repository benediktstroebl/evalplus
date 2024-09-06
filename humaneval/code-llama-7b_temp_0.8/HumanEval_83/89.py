
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def total_digits(n):
        return n * 9 + 1

    def at_least_one_starts(n):
        # 1 + 2 + ... + 9 + 1 = 45
        return total_digits(n) * 10 - 45

    def one_starts(n):
        # 11 + 12 + ... + 19
        return 9 * (total_digits(n) - 1)

    def no_one_starts(n):
        # 2 + 3 + ... + 9
        return 8 * total_digits(n)

    return (
        at_least_one_starts(n) -
        one_starts(n) -
        no_one_starts(n)
    )

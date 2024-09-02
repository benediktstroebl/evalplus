
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def count_n_digit(n):
        count = 0
        for i in range(1, 10 ** n):
            digits = str(i)
            if digits[0] == "1" or digits[-1] == "1":
                count += 1
        return count
    if n == 1:
        return 1
    return count_n_digit(n - 1) + count_n_digit(n)

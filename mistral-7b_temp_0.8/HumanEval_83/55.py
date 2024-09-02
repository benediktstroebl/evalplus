
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def count_one_start(n):
        count = 0
        while n > 0:
            first_digit = n % 10
            if first_digit == 1:
                count += 1
            n = n // 10
        return count

    def count_one_end(n):
        count = 0
        while n > 0:
            last_digit = n % 10
            if last_digit == 1:
                count += 1
            n = n // 10
        return count

    return count_one_start(n) + count_one_end(n)

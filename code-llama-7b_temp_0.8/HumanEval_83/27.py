
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def count_one_digits(n, count):
        if n == 0:
            return count

        # a 1 in the leftmost digit is possible
        count += 10

        # the number of 1-digits in this n-digit number is the
        # number of n-digit numbers that have 1 as their last digit,
        # so 10 times the number of (n-1)-digit numbers that start or end with 1
        # and subtract 10 since the 10 in the first digit of this number
        # doesn't count
        return count_one_digits(n - 1, 10 * count - 10)

    count = 0
    count += count_one_digits(n - 1, 0)
    count += count_one_digits(n - 1, 1)
    return count

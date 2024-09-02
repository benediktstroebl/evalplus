
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def nth_digit(num, n):
        return num % (10**n) // (10**(n-1))

    def starts_one(num):
        return nth_digit(num, 1) == 1

    def ends_one(num):
        return nth_digit(num, n) == 1

    def count_digits(func, n):
        return sum(func(num) for num in range(1, 10**n))

    return count_digits(starts_one, n) + count_digits(ends_one, n) - 1



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def is_one(s):
        return s.startswith('1') or s.endswith('1')

    def is_valid_length(s):
        return len(s) == n

    def is_valid(s):
        return is_valid_length(s) and is_one(s)

    num_of_digits = 10 ** (n - 1)
    return sum(map(is_valid, str(num_of_digits)))



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    def count_str(s):
        return round((s.count('1') /
                      (s.count('1') + s.count('0'))) * n)

    return sum(count_str(str(x)) for x in range(1, 1001))



def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    def count(digits, one_start, one_end):
        if digits == 1:
            if one_start:
                return 1
            if one_end:
                return 1
            return 0
        num = count(digits-1, one_start, one_end)
        if one_start:
            num += count(digits-1, True, one_start)
        if one_end:
            num += count(digits-1, one_end, True)
        return num
    return count(n, True, True)

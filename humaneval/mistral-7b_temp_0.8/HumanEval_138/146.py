
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0:
        return False

    def helper(n, start, m):
        if n == 0 and start != 0:
            return True
        if m == 4:
            return False
        return helper(n, start + 4, m + 1) or helper(n - start, start + 2, m + 1)

    return helper(n, 2, 0)


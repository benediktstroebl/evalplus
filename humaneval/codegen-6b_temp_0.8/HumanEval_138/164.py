
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4:
        return False
    def __is_equal_to_sum_even(n):
        return sum([i for i in range(0, n, 2) if i > 0]) == n
    return __is_equal_to_sum_even(n)

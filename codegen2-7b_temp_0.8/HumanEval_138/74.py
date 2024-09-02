
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0:
        return False
    if n == 4 or n == 6 or n == 8:
        return True
    if n % 2 == 1 and n > 2:
        return is_equal_to_sum_even(n - 1) or is_equal_to_sum_even(n + 1)
    return is_equal_to_sum_even(n - 2

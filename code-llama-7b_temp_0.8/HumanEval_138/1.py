
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # The sum of 4 even numbers must be even.
    if n % 2 != 0:
        return False
    for i in range(2, n // 2 + 1):
        if n - 2 * i * (i - 1) == 0:
            return True
    return False


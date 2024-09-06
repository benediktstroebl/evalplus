
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n % 4 != 0):
        return False
    for i in range(n):
        if n == i + 2 * (i + 1) + 2 * (i + 2) + 2 * (i + 3):
            return True


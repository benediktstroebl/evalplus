
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if is_sum_even(n):
        return True
    if not is_sum_even(n):
        return False
    if n < 4:
        return False
    return n % 4 == 0


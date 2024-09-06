
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False
    # or just return not n % 2
    if n % 2 != 0:
        n -= 1
    while n > 0:
        if is_sum_of_4_even(n):
            return True
        n -= 2
    return False


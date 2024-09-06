
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    s = (n >> 1) << 1
    for i in xrange(7, int(s), 2):
        if not is_equal_to_sum_even(s - i):
            return False
    return True


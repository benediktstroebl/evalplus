
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4:
        return False
    if n % 2 != 0:
        return False
    for i in xrange(3, n/2):
        if n - i * 2 == 0 and i % 2 == 0:
            return True
    return False


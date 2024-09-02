
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1 or n < 8:
        return False
    s = 0
    for i in range(1, 5):
        s += 2 * i
        if s == n:
            return True
    return False


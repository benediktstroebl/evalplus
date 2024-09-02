
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:
        return False

    n_div_2 = n / 2
    s = n_div_2
    while s % 2 == 0:
        s = s / 2
        if s == 1:
            return True
    return False


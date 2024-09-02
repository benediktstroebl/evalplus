
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n_1 = n + 1
    n_2 = n / 2
    n_3 = (n_2 * (n_1 - n_2)) / 2
    if n_3 == n:
        return True
    else:
        return False


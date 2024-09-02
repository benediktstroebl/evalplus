
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    result = False
    n_check = n
    while n_check > 0:
        if n_check % 2 == 0:
            n_check = n_check // 2
        else:
            return False
    return True


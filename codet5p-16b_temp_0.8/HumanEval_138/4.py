
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n_str = str(n)
    return any([eval(f'{n_str}{i}') % 2 == 0 and eval(f'{n_str}{i}') % 2 == 0 for i in range(0, len(n_str))])

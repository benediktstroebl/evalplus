
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n_set = set([i for i in range(2, n) if i % 2 == 0])

    for i in range(2, n):
        if n - i in n_set:
            return True
    return False


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    return n % 2 == 0 and sum(n for n in range(1, 5) if n % 2 == 0 and n <= n) == 4
    pass

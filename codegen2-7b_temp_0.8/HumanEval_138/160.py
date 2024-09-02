
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4:
        return False
    if n % 2 == 1:
        return False
    return sum(2 * x for x in range(1, int(n / 2) + 1) if x % 2 == 0) ==

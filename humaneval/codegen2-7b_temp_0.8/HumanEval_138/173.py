
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = abs(n)
    if n < 4:
        return False
    for i in range(4, n // 2 + 1, 2):
        if n % i == 0:
            return True
    return False

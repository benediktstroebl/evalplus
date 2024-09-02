
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0 or n > 10:
        return False
    if n % 2 != 0:
        return False
    if n % 4 != 0:
        return False
    if n // 2 != n:
        return False
    for i in range(3, int(n ** 0.5) + 1):
        if n - i ** 2 != i:
            return False
    return True

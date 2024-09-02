
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n > 8:
        return False
    if n in [2, 4, 6, 8]:
        return True
    if n % 2 != 0:
        return False
    x = int(n // 2)
    y = n - x * 2
    if x > 2 and y % 2 == 0:
        return False
    if y > 0:
        return True
    return False

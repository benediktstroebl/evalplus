
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0 or n % 2 == 0:
        return False
    if n % 4 == 0:
        return True
    x = n // 4
    if n % 4 != x**2 + x:
        return False
    y = x + 1
    if n % 4 != y**2 + y:
        return False
    z = x + 2
    if n % 4 != z**2 + z:
        return False
    return True
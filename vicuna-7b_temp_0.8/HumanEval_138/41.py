
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0:
        return False
    if n % 2 == 0:
        return False
    if n % 4 == 0:
        return False
    if n % 6 == 0:
        return False
    if n % 8 == 0:
        return False
    if n % 10 == 0:
        return False
    if n % 12 == 0:
        return False
    if n % 14 == 0:
        return False
    if n % 16 == 0:
        return False
    if n % 18 == 0:
        return False
    if n % 20 == 0:
        return False
    return True

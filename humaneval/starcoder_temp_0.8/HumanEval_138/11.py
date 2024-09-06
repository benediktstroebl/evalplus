
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 10:
        return False
    if n % 2:
        return False
    for i in range(10, n, 2):
        if n == i or n == i + 2 or n == i + 4:
            return True
        if n < i + 6:
            return False
    return False



def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n > 15:
        return False
    if n % 2 == 0 and n % 4 == 0:
        return True
    for i in range(2, n):
        if n % i == 0 and i != n / 2:
            return False
    return True

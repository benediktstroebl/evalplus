
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even
    if n % 2 == 0:
        return False
    # Check if n is 4 or 6
    if n in (4, 6):
        return False
    # Check if n can be expressed as the sum of 4 positive even numbers
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

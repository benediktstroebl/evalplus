
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0 or n % 2 != 0:
        return False
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

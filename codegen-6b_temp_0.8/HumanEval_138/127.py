
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4: return False
    if (n % 2 != 0): return False
    if is_prime(n): return False
    for i in range(4, n, 2):
        if is_even(i):
            if is_prime(n - i):
                return True
    return False

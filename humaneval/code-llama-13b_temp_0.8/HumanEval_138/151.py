
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    i = 1
    found = 0
    while i * i <= n:
        if n - i * i >= 0:
            if (i % 2 == 0) and (n - i * i) % 2 == 0:
                found += 1
        i += 1
    return found >= 4



def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if not is_even(n):
        return False
    n = abs(n)
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            if is_even(i) and is_even(n - i):
                return True
    return False

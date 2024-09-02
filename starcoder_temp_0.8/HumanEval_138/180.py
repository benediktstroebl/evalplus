
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4:
        return False
    for i in range(n // 2 + 1):
        if n - 2 * i <= 2 * i:
            break
        if not is_even(n - 2 * i):
            continue
        if i == n // 2 - i:
            return True
    return False

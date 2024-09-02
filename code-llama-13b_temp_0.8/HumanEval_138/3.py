
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0:
        return False
    n_sum = 0
    for i in range(1, (n // 2) + 1):
        for j in range(1, (n // 2) + 1):
            if i + j == n - i - j:
                return True
    return False


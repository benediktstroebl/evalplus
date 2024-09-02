
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0 or n % 2 == 1:
        return False

    for a in range(1, n // 2 + 1):
        for b in range(1, n // 2 + 1):
            for c in range(1, n // 2 + 1):
                if a + b + c == n:
                    return True
    return False


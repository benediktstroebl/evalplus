
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return False

    for i in range(1, n // 2 + 1):
        if n - i > 0 and (n - i) % 2 == 0:
            for j in range(1, (n - i) // 2 + 1):
                if (n - i - j) > 0 and (n - i - j) % 2 == 0:
                    for k in range(1, (n - i - j) // 2 + 1):
                        if n - i - j - k == i:
                            return True
    return False


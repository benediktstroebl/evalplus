
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 0 and n > 0:
        for i in range(1, n):
            if (n - i) % 2 == 0:
                if (n - 2 * i) % 2 == 0:
                    if (n - 3 * i) % 2 == 0:
                        if (n - 4 * i) % 2 == 0:
                            return True
    return False

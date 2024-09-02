
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    assert (n > 0)
    if (n % 2 == 0):
        for i in range(1, n-1, 2):
            for j in range(i + 1, n - 1, 2):
                if (n - (i+j) % 2 == 0 and n - i - j > 0):
                    return True
    return False

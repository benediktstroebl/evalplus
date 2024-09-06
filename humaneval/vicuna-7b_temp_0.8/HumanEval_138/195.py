
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 4:
        return False
    elif n % 2 != 0:
        return False
    elif n // 2 == 2 or n // 2 == 4:
        return False
    else:
        for i in range(2, n-1):
            if (n - i - 1) % 2 == 0:
                return False
        return True

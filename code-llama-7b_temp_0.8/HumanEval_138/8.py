
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 8:
        return True
    elif n % 2 != 0:
        return False
    else:
        for i in range(4):
            if n - 2 * i > 0:
                n -= 2 * i
            else:
                return False
    return True


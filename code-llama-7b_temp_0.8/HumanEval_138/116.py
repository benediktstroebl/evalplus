
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n % 4 == 0):
        a = n // 4
        if ((a % 2 == 0) and (a >= 8)):
            return True
        else:
            return False
    else:
        return False


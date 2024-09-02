
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(2, int(n / 2), 2):
        if 0 < (n - (i * i)):
            if (n - (i * i) == i):
                return True
    return False


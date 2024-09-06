
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(1, int(n / 2)):
        j = i * 2
        if n - i - j == 0:
            return True
        if n - i - j > 0:
            if is_even(n - i - j) == True:
                return True
    return False


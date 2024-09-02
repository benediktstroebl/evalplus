
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    s = n // 2
    if s == 0:
        return n % 2 == 0
    elif s % 2 == 0:
        return is_equal_to_sum_even(s)
    else:
        return is_equal_to_sum_even(s + 1

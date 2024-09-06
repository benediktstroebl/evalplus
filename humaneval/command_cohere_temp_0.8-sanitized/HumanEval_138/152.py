def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    """
    if n < 0:
        return False
    elif n % 2 == 1:
        return False
    else:
        half_n = n // 2
        return half_n % 2 == 0
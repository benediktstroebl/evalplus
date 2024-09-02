
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    count_even = 0
    count_odd = 0
    if n < 4:
        return False
    while n >= 1:
        if n % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        n -= 1
    if count_even == 4:
        return True
    else:
        return False

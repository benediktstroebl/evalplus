
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0 or n % 2 != 0:
        return False
    num = 1
    while num <= n/4:
        if num <= n/2:
            if n - 2*num == 0:
                return True
        else:
            if 2*num - n == 0:
                return True
        num += 1
    return False

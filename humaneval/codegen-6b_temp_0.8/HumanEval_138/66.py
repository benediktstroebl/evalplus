
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a, sub_sum = n // 2, n
    i = 1
    while sub_sum - 4*i*2 >= 0:
        sub_sum -= 4*i*2
        i += 1
    if sub_sum == 0:
        return True
    else:
        return False


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_even = 0
    i = 1
    while sum_even < n:
        if n-sum_even <= 0:
            return False
        sum_even += 2*i
        i += 1
    return True




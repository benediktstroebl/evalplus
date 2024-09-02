
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum = 0
    a = 2
    while sum < n:
        sum = a + a + a + a
        if sum == n:
            return True
        a += 2
    return False

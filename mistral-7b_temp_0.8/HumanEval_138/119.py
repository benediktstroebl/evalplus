
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_ = 0
    for i in range(1, int(n/2) + 1):
        for j in range(1, int(n/2) + 1):
            sum_ = 2 * i + 2 * j
            if sum_ == n:
                return True
    return False


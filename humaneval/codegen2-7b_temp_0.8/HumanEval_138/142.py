
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0:
        return False

    for k in range(1, int(n**0.5)+1):
        if is_equal_to_sum_even(k) and is_equal_to_sum_even(n-k):
            return True

    return

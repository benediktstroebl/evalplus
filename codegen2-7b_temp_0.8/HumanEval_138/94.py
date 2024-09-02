
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0 or n == 1:
        return True
    for i in range(3, n // 2 + 1):
        if n % i == 0 and is_equal_to_sum_even(i) and is_equal_to_sum_even(n - i):
            return True
    return

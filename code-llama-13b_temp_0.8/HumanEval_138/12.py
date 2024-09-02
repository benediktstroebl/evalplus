
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1:
        return False
    n /= 2
    s = 0
    for i in range(5):
        if n - i >= 0:
            s += n - i
        else:
            return False
    return s == n


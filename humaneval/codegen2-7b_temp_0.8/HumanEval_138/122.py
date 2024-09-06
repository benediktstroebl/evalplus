
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    i = 2
    while i < n:
        if n % i == 0 and i % 2 == 0:
            i += 2
            n -= 1
        else:
            i += 1
    if n == 1:
        return True
    else:
        return False

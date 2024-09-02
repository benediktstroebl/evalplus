
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 != 0:
        return False
    i = 2
    while i <= n / 2:
        if n % i == 0 and n / i % 2 == 0:
            if n / i == i:
                return True
            else:
                i += 2
    return False


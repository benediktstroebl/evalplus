
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    a = 2
    b = 2
    while a < n / 2:
        while b < n / 2:
            if a + b == n:
                return True
            b = b + 2
        a = a + 2
        b = 2
    return False


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0:
        return False
    if n <= 4:
        return n % 2 == 0
    else:
        result = is_equal_to_sum_even(n - 4)
        if result:
            return True
        else:
            return is_equal_to_sum_even(n - 2)

assert is_equal_to_sum_even(4) == False
assert is_equal_to_sum_even(6) == False
assert is_equal_to_sum_even(8) == True
assert is_equal_to_sum_even(100) == False
assert is_equal_to_sum_even(999999) == False

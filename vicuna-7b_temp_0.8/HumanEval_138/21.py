
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 0 or n > 10:
        return False
    for i in range(1, n):
        if (n % i == 0) and (n // i >= 2):
            return False
    return True

@pytest.mark.parametrize("n", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

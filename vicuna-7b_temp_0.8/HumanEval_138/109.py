
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    even_sum = 0
    for i in range(3, n):
        even_sum += i
    if n - even_sum in (0, 2, 4, 6):
        return True
    return False

@pytest.mark.parametrize("n", range(1, 11))

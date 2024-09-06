
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    i, j = 4, 6
    while i != j:
        if i % 2 == 0 and j % 2 == 0 and n == i + j:
            return True
        i += 1
        j -= 1
    return False


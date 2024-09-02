
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    for i in range(n):
        if i % 2 == 0:
            if (i + 1) % 2 == 0 and (i + 2) % 2 == 0 and (i + 3) % 2 == 0 and (i + 4) % 2 == 0:
                return True
    return False

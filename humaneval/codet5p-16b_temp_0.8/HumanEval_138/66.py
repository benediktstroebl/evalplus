
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    for i in range(0, n):
        for j in range(0, i):
            if (i + j + 2) % 2 == 0 and (i + j + 2) in range(2, n):
                return True
    return False

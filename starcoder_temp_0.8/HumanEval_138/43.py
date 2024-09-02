
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Your code here
    if n < 10:
        if n % 2 == 0:
            return True
        else:
            return False

    if n % 10 in [2, 4, 6, 8]:
        return is_equal_to_sum_even(n // 10)
    else:
        return False

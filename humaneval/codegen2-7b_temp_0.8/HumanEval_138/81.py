
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if is_sum_of_4_positive_even_numbers(n) and is_sum_of_2_positive_even_numbers(n):
        return True
    else:
        return False


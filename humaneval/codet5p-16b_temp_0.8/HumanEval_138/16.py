
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    return is_equal_to_sum_even_even(n) and is_equal_to_sum_even_even(n-1) and is_equal_to_sum_even_even(n-2)
    

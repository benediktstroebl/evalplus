
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is a multiple of 4
    if n % 4 != 0:
        return False
    
    # If n is a multiple of 4, check if it is a multiple of 8
    if n % 8 == 0:
        return False
    
    # If n is neither a multiple of 4 nor a multiple of 8, it must be a multiple of 16
    if n % 16 == 0:
        return True
    else:
        return False

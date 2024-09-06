
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return True
    elif n == 1:
        return False
    elif n == 2:
        return False
    elif n == 3:
        return False
    elif n == 4:
        return True
    else:
        return False
    
    
    

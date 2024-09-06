
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    
    def is_even(n):
        """Evaluate whether the given number n is even
        Example
        is_even(4) == True
        is_even(6) == True
        is_even(8) == True
        """
        
        if n % 2 == 0:
            return True
        else:
            return False
    
    def is_sum_even(n):
        """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
        Example
        is_equal_to_sum_even(4) == False
        is_equal_to_sum_even(6) == False
        is_equal_to_sum_even(8) == True
        """
        
        if n % 4 == 0:
            return True
        else:
            return False
    
    if is_even(n) and is_sum_even(n):
        return True
    else:
        return False
        

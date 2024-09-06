
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2 == 0:
        a = n/4
        b = a + 1
        c = a + 2
        d = a + 3
        if a.is_integer() and b.is_integer() and c.is_integer() and d.is_integer():
            return True
        else:
            return False
    else:
        return False
    

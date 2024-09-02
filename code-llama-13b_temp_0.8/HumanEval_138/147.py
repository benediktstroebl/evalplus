
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    assert n > 0
    
    if n % 2 == 1:
        return False
    else:
        n = n // 2
        res = 0
        for i in range(1, 5):
            if n % 2 == 0:
                res += n
                n = n // 2
            else:
                return False
        
        if n == 0:
            return True
        else:
            return False

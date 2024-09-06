
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    x=n-2
    y=n-4
    z=n-6
    if (x+y+z+n==4*n) and (x>0) and (y>0) and (z>0):
        return True
    else:
        return False

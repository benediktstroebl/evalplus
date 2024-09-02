
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    
    if n % 2 == 1:
        return False
    
    sum_odd = n // 2
    sum_even = sum_odd * 2
    if sum_odd > sum_even:
        sum_even += 1
    
    if sum_even == n:
        return True
    else:
        return False

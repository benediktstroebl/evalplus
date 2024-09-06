
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0 or n > 100:
        return False
    
    if n % 2 != 0:
        return True
    
    result = 0
    for i in range(1, (n+1)/2):
        result += i
    
    return (result % 4) == 0

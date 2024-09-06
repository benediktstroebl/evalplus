
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    
    n_str = str(n)
    
    for i in range(1, len(n_str) + 1):
        if i % 2 == 0:
            if int(n_str[:i]) % 2 == 0 and int(n_str[i:]) % 2 == 0:
                if int(n_str[:i]) + int(n_str[i:]) == n:
                    return True
                
    return False
    


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even
    if n % 2 != 0:
        return False
    
    # Check if n is less than 4
    if n <= 3:
        return False
    
    # Check if n is divisible by 4
    if n % 4 == 0:
        return False
    
    # Check if n is divisible by 8
    if n % 8 == 0:
        return False
    
    # Check if n is divisible by 16
    if n % 16 == 0:
        return False
    
    # Check if n is divisible by 32
    if n % 32 == 0:
        return False
    
    # Check if n is divisible by 64
    if n % 64 == 0:
        return False
    
    # Check if n is divisible by 128
    if n % 128 == 0:
        return False
    
    # Check if n is divisible by 256
    if n % 256 == 0:
        return False
    
    # Check if n is divisible by 512
    if n % 512 == 0:
        return False
    
    # Check if n is divisible by 1024
    if n % 1024 == 0:
        return False
    
    # Check if n is divisible by 2048
    if n % 2048 == 0:
        return False
    
    # Check if n is divisible by 4096
    if n % 4096 == 0:
        return False
    
    # If none of the above conditions are satisfied, return True
    return True

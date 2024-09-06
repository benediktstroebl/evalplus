
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # check if n is divisible by 2
    if n % 2 != 0:
        return False
    
    # check if n is divisible by 4
    if n % 4 != 0:
        return False
    
    # check if n is divisible by 8
    if n % 8 != 0:
        return False
    
    # check if n is even
    if n % 2 != 0:
        return False
    
    # check if n is a multiple of 4
    if n % 4 == 0:
        return False
    
    # check if n is a multiple of 8
    if n % 8 == 0:
        return False
    
    # check if n is a multiple of 16
    if n % 16 == 0:
        return False
    
    # check if n is a multiple of 32
    if n % 32 == 0:
        return False
    
    # check if n is a multiple of 64
    if n % 64 == 0:
        return False
    
    # check if n is a multiple of 128
    if n % 128 == 0:
        return False
    
    # check if n is a multiple of 256
    if n % 256 == 0:
        return False
    
    # check if n is a multiple of 512
    if n % 512 == 0:
        return False
    
    # check if n is a multiple of 1024
    if n % 1024 == 0:
        return False
    
    # check if n is a multiple of 2048
    if n % 2048 == 0:
        return False
    
    # check if n is a multiple of 4096
    if n % 4096 == 0:
        return False
    
    # check if n is a multiple of 8192
    if n % 8192 == 0:
        return False
    
    # check if n is a multiple of 

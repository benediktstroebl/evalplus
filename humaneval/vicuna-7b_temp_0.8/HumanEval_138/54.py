
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check for cases where the number is less than 5
    if n < 5:
        return False
    
    # Check for cases where the number is divisible by 2, 3, 4, 5
    if n % 2 == 0 or n % 3 == 0 or n % 4 == 0 or n % 5 == 0:
        return False
    
    # Check if the number is divisible by 10
    if n % 10 == 0:
        return False
    
    # Check if the number is even and greater than 10
    if n % 2 == 0 and n > 10:
        # Find the largest prime factor of the number
        factors = factor(n)
        
        # Check if the number can be expressed as the sum of 4 positive even numbers
        return sum(i % 2 == 0 and i > 1 for i in factors) == 4
    else:
        return False
    

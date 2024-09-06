
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int=x
    For example:
    is_simple_power(1, 4) => true
    is_simple_power(2, 2) => true
    is_simple_power(8, 2) => true
    is_simple_power(3, 2) => false
    is_simple_power(3, 1) => false
    is_simple_power(5, 3) => false
    """
    # Check if n is zero
    if n == 0:
        return x == 1
    
    # Check if x is equal to n
    if x == n:
        return True
    
    # Check if x is equal to the square of n
    if x == n**2:
        return True
    
    # If x is not equal to n and not equal to n^2, then check if n is a prime number
    if n % 2 != 0:
        # If n is odd, then x must be a power of 2
        if 2**int(n) == x:
            return True
        
    return False
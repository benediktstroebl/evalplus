
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
        return True
    
    # Check if x is equal to n**int
    if x == n**int:
        return True
    
    # Check if x is a power of n
    if n == int(n):
        return is_simple_power(x, n//int(n))
    
    # Check if x is a power of n-1
    if x == n**int//int(n):
        return is_simple_power(x, n-1)
    
    # Check if x is equal to n**int+1
    if x == (n+1)**int - (1//int(n)):
        return True
    
    # Check if x is a power of n-1
    if x == (n+1)**int//int(n-1):
        return is_simple_power(x, n-1)
    
    # If none of the above checks pass, return False
    return False
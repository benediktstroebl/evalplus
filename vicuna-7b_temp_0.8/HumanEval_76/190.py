
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
    # Check if x is divisible by n
    if not (x % n):
        return False
    
    # Calculate int(x/n)
    int_part = int(x / n)
    
    # Check if int(x/n) is equal to x
    if int_part != x:
        return False
    
    # If x is divisible by n and int(x/n) is equal to x then x is a simple power of n
    return True



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
    # base case: 0 is not a simple power of anything
    if x == 0:
        return False
    
    # base case: 1 is a simple power of everything (including 1)
    elif n == 1:
        return True
    
    # recursively find if n is a simple power of x
    else:
        # check if x is a simple power of n
        if n % x == 0:
            # recursively check if n is a simple power of x/n
            return is_simple_power(x/n, n)
        
        # x is not a simple power of n
        else:
            return False

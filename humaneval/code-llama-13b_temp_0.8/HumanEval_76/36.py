
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
    # Your code here
    if n == 1:
        return x == 1
    
    if n == 2:
        return x != 2 and x % 2 == 0
    
    if n == 3:
        return (x == 3 or (x % 3 == 0 and x % 9 == 0))
    
    if n == 4:
        return (x == 4 or x == 16 or (x % 4 == 0 and x % 6 == 0 and x % 9 == 0))
    
    if n == 5:
        return (x == 5 or x == 25 or (x % 5 == 0 and x % 25 == 0))
    
    if n == 6:
        return (x == 6 or x == 36 or (x % 6 == 0 and x % 9 == 0 and x % 36 == 0))
    
    if n == 7:
        return (x == 7 or (x % 7 == 0 and x % 49 == 0))
    
    if n == 8:
        return (x == 8 or x == 64 or (x % 8 == 0 and x % 27 == 0 and x % 81 == 0))
    
    if n == 9:
        return (x == 9 or x == 81 or (x % 9 == 0 and x % 36 == 0 and x % 81 == 0))


    if n == 10:
        return (x == 10 or x == 100 or (x % 10 == 0 and x % 100 == 0 and x % 900 == 0))
    
    return False
    
    
    

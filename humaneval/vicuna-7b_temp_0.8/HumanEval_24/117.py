

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Check if n is divisible by 2
    if n % 2 == 0:
        return 2
    
    # Check if n is divisible by 3
    if n % 3 == 0:
        return 3
    
    # Check if n is divisible by 4
    if n % 4 == 0:
        return 4
    
    # Check if n is divisible by 5
    if n % 5 == 0:
        return 5
    
    # Check if n is divisible by 6
    if n % 6 == 0:
        return 6
    
    # If none of the above conditions are met, the largest divisor is n
    return n
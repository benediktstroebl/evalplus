
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is prime
    if a % 2 == 1:
        return False
    
    # Check if a is divisible by 3
    if a % 3 == 0:
        return False
    
    # Check if a is divisible by 5
    if a % 5 == 0:
        return False
    
    # Check if a is divisible by 7
    if a % 7 == 0:
        return False
    
    # Check if a is divisible by 11
    if a % 11 == 0:
        return False
    
    # Check if a is less than 100
    if a < 100:
        # Check if a is divisible by any prime number less than 50
        for i in range(50, a, 2):
            if i % 2 == 0:
                return False
            if i % 3 == 0:
                return False
            if i % 5 == 0:
                return False
            if i % 7 == 0:
                return False
            if i % 11 == 0:
                return False
    
    # If a is greater than 100 or we have reached the end of the loop, then a is prime
    return True

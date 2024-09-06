
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 1:
        return False
    if a < 100:
        counter = 2
        while counter <= a:
            if a % counter == 0:
                if a / counter > 1 and a / counter < 100:
                    return True
            counter += 1
        return False
    return False
    

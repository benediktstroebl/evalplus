
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a<100:
        i=1
        while i<100:
            if is_prime(a)==True:
                i=i+1
                a=a/10
                return is_multiply_prime(a)
            else:
                return False
    else:
        return True
    

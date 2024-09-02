
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        for i in xrange(2,a):
            n = 0
            n = i*2
            while n < a:
                if n == i:
                    n += 2
                    continue
                else:
                    n += i
            if n == a:
                continue
            else:
                return False
        return True
    
    return False


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    
    primes = [2, 3, 5, 7]
    
    for i in range(11, a):
        
        if i % 2!= 0:
            if i % 3!= 0:
                if i % 5!= 0:
                    if i % 7!= 0:
                        if i % 2!= 0 and i % 3!= 0 and i % 5!= 0 and i % 7!= 0:
                            primes.append(i)
    
    if a in primes:
        return True
    else:
        return False


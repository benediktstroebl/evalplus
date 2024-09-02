
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    primes = []
    for i in range(2,int(a**.5)+1):
        if is_prime(i):
            primes.append(i)
    
    if any(a % p == 0 for p in primes):
        return False
    
    for i in range(3,len(primes)):
        if all(a % p!= 0 for p in primes[:i]):
            return True
    return False
    


def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    #Multiply primes are easy
    #Two and three are primes
    #All multiples of 5 are not primes
    #When multiplying by 5, you need to not have a factor of 5 or 3
    
    #Default to False
    #If there is a prime found, make true
    #If prime is false, return False
    
    prime_found = False
    
    #Check for 2 and 3
    if a % 2 == 0 or a % 3 == 0:
        prime_found = True
    
    #Check if any of the other factors are 5, 7, or 11
    for i in range(5, 12):
        if a % i == 0:
            prime_found = True
            
    if a % 5 == 0:
        prime_found = False
            
    return prime_found

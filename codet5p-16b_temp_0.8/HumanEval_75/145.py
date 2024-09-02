
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    is_prime = lambda x: not [i for i in range(2, x) if x % i == 0] # Can probably be done with a list comprehension
    prime_factors = lambda a: [i for i in range(2, a) if is_prime(i) and a % i == 0]
    p = prime_factors(a)
    if len(p) == 3:
        return True
    return False
    
    

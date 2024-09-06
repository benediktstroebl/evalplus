
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Using the Sieve of Eratosthenes to check if the number is prime
    is_prime = [True for i in range(a) if (a % i) == 0]
    
    # Using a while loop to check if the number is the multiplication of 3 prime numbers
    while True:
        p = 2
        while p < a:
            if a % p == 0:
                break
            p += 1
        if p == a:
            return False
        p = 3
        while p * p <= a:
            if a % (p * p) == 0:
                break
            p += 1
        if p * p == a:
            return True
    
    # If no prime factor is found, return True
    return True

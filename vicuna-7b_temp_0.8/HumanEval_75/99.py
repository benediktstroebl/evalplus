
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Use the Sieve of Eratosthenes to check if the number is prime
    # Use the Euclid's algorithm to check if the number is the product of two prime numbers
    if a <= 100:
        is_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_prime = False
                break
        if is_prime:
            for p in primes:
                if (a // p) % p == 0:
                    is_prime = False
                    break
        return is_prime
    else:
        return False
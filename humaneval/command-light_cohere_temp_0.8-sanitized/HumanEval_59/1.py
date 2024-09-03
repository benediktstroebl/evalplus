import math
def largest_prime_factor(n: int):
    if n <= 1:
        return 1
    if n <= 3:
        return 3
    
    # Calculate the number of primes less than or equal to sqrt(n)
    sqrt_n = int(math.sqrt(n))
    count = 0
    while count < sqrt_n and n % prime != 0:
        count += 1
        prime = n // prime  # For the next iteration
        n = n // prime
    
    return prime
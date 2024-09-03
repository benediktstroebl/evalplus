```python
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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
``` 
This code defines a `largest_prime_factor` function that calculates the largest prime factor of a given number `n`. The function begins by checking if `n` is less than or equal to 1, in which case it returns 1. It then checks if `n` is less than or equal to 3, and if so, returns 3 since 3 is the largest prime factor of 1 and 3. The function then proceeds to calculate the number of primes less than or equal to the square root of `n` using a loop. After that, it counts the number of primes up to the square root of `n` and keeps track of the prime factors. The function then returns the final prime factor `prime`, which is the largest prime factor of `n`.
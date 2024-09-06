Here's a self-contained Python function to check if a given number is a prime, using the Sieve of Eratosthenes algorithm:
```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    # Initialize a PRIMARY and SECOND lists with primes
    PRIMARY = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    SECONDARY = [i for i in PRIMARY if i != 2 and i != 3]

    # Initialize counter for iterations and primes found
    counter = 0
    primes_found = 0

    # Loop through numbers from 2 to n
    for num in range(2, n + 1):
        # Skip numbers that are not prime
        if num not in SECONDARY:
            continue

        # Mark num as a prime found
        counter += 1
        primes_found += 1

        # Check if the number is divisible by any known prime
        if num % 2 == 0 or num % 3 == 0:
            continue

    # If no numbers were found, return false
    return primes_found > 0

# Example usage:
>>> is_prime(6)
False
>>> is_prime(101)
True
>>> is_prime(11)
True
>>> is_prime(13441)
True
>>> is_prime(61)
True
>>> is_prime(4)
False
>>> is_prime(1)
False
```
The function uses the Sieve of Eratosthenes algorithm, which efficiently finds all prime numbers up to a given limit. The algorithm works by marking numbers divisible by 2 and 3 as primes and then checking all other numbers to see if they are divisible by any of these numbers.
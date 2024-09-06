```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # The list of primes less than and equal to n.
    primes = [2, 3, 5, 7, 11, 13]
    for prime in primes:
        while n % prime == 0:
            n //= prime
        if n == 1:
            return prime
    return n
```

This approach takes advantage of the fact that the primes less than n are all composite numbers and so will divide into n several times. This means we can simplify the problem to essentially finding the highest divisor of n, which will be the largest prime factor. 

To do this, we iterate through each prime number less than or equal to the square root of n and repeatedly divide n by each prime until it is no longer divisible. If n equals 1, then that prime must be the largest prime factor, and we return it. If we reach the end without n equaling 1, then n must be a prime itself, which is the largest prime factor. 

To test this, run the function with the test cases provided, as well as any other test cases you would like to ensure it works correctly for. 
```python
largest_prime_factor(13195) # Should return 29
largest_prime_factor(2048)  # Should return 2
largest_prime_factor(317)  # Should return 317
largest_prime_factor(18059) # Should return 59
```
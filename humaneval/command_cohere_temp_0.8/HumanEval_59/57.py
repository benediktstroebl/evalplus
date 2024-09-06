```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Test if n is 2 or 3, these are the smallest prime numbers
    if n == 2 or n == 3:
        return n
    # Check if n is divisible by 2 or 3, the smallest prime numbers
    while n % 2 == 0 or n % 3 == 0:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
    # Check for prime factors from 5 to sqrt(n)
    for i in range(5, int(n**0.5) + 1, 6):
        while n % i == 0:
            n //= i
    # If n has reached 1, it means it was a prime number
    if n == 1:
        return n
    # In the unlikely event that n is a prime factor greater than sqrt(n)
    while n % 5 == 0:
        n //= 5
    # If n is still greater than 2, it must be a prime number
    if n > 2:
        return n
    return 2  # Return 2 if n is 2
```

This algorithm optimizes the search for the largest prime factor of a given number `n`. It begins by checking if `n` is divisible by 2 or 3, the smallest prime numbers. Then, it iterates through prime numbers in increments of 6, starting from 5 and iterating up to the square root of `n`, to efficiently cover the search space of potential prime factors. 

If `n` is not eliminated by any of these checks, it is a prime number itself or has a prime factor greater than its square root. In either case, it falls back to checking for divisibility by prime numbers greater than 2. Finally, the algorithm handles the cases where `n` is 2, which is a special case in the problem statement, and ensures that 2 is correctly returned for such inputs.  This approach balances efficiency and simplicity while solving the problem.
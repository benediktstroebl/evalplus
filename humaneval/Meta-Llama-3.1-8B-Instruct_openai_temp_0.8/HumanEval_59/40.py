### Largest Prime Factor
#### Python Script
```markdown
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This Python script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It does this by continuously dividing `n` by the smallest divisor (starting from 2) until it finds a divisor, then it updates `n` to be the quotient and repeats the process. The loop ends when the divisor is greater than the square root of `n`, at which point `n` is the largest prime factor.
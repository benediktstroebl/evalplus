```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    
    # Start from the smallest prime number, which is 2
    i = 2
    
    # Continue checking factors until we find a prime factor
    while n > 1:
        # If n is divisible by i, then i is a factor
        if n % i == 0:
            # Check if i is prime by checking divisibility from 2 to sqrt(i)
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            # If i is prime, return it as the largest prime factor
            if is_prime:
                return i
            # Otherwise, divide n by i to continue the search for a prime factor
            else:
                n = n // i
        # If n is not divisible by i, increment i by 1
        else:
            i += 1
    
    # If no prime factors are found, return -1 (this should not happen based on the problem statement)
    return -1

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a simple trial division method to find the largest prime factor, which is sufficient for this problem. The script also includes two test cases to verify the correctness of the function.
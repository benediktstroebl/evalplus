```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, smaller than n.
    """
    prime_factors = []
    is_prime = [True] * (n+1)
    is_prime[0] = False  # 0 is not a prime
    is_prime[1] = False  # 1 is not a prime
    
    for p in range(2, n+1):
        if is_prime[p]:
            prime_factors.append(p)
            is_prime[p] = False
    
    # Calculate the largest divisor as max(prime_factors)
    largest_divisor = max(prime_factors)
    
    return largest_divisor
```
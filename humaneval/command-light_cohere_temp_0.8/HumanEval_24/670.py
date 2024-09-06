```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest number that divides n evenly, smaller than n
    Returns: The largest such number
    """
    # Make sure n is positive
    n = n if n >= 0 else 0
    
    # Use lightning fast power calculation to get the prime factorization
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n /= 2
    while n > 1:
        n //= gcd(n, factors[-1]))
        factors.append(factors[-1])
    
    # Find the largest divisor among the factors
    return max(factors, key=lambda x: x // n)
```
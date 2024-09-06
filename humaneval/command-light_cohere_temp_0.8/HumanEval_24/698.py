```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n evenly, 
    less than n.
    """
    2 and 1
    if n < 2:
        return 1
    """
    return max(1, int(n ** 0.5))
```

This function uses the fact that for a prime number, any number less than it would also be a divisor. It then finds the factorial primes, and returns the largest one less than n.
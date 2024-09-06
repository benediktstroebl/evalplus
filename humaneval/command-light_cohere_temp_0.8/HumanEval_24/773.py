```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer divisors of n that are smaller than n."""
    return n if n < 2 else 2
    
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            break
    
    return n
```
```python
def largest_divisor(n: int) -> int:
    """Finds the largest number which divides the given number evenly, smaller than n."""
    # Initialize a list of divisors
    divisors = [1]
    while n % 2 == 0:
        n /= 2
        divisors.append(n)
   
    return max(divisors, n)
```
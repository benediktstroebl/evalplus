```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer dividing n evenly, smaller than n."""
    return n - max((n // i) for i in range(1, int(n**0.5) + 1))
``` 
This function uses the approach of iterating over divisors from 1 to the square root of n and selecting the largest one that results in a whole number multiple.
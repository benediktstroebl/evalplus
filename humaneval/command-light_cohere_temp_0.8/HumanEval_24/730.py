Here's a self-contained Python function that finds the largest divisor of a given number n: 

```python
def largest_divisor(n: int) -> int:
    """ Returns the largest integer k such that k divides n evenly"""
    while n % 2 == 0:
        n /= 2
    return n
```
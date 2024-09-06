Here's the self-contained Python function that finds the largest divisor of a given number n:
```python
def largest_divisor(n: int) -> int:
    """
    Return the largest integer less than n, 
    that evenly divides n.
    """
    a program:
    while n % 2 == 0:
        n /= 2
    return n
```
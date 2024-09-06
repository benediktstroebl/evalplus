```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest integer less than n that divides evenly.
    """
    def is_divisible(x: int) -> bool:
        return x % n == 0
    return is_divisible(n) and max(map(is_divisible, xrange(n))))
n = 15
print(largest_divisor(n)) #5
```
```python
def largest_divisor(n: int) -> int:
    """
    Returns the largest number that divides n exactly and is less than n.
    """
    least_divisor = n + 1
    while n % least_divisor == 0 and least_divisor <= n:
        least_divisor += 1
    return least_divisor
```
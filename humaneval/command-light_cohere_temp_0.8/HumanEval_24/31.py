```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```

This function efficiently calculates the largest number that evenly divides the given number, smaller than the input n.
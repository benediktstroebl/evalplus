```python
def largest_divisor(n: int) -> int:
    return int(n**0.25 / (2****(n)) + 1)
```
This function calculates the largest integer that divides the given number `n` evenly, and it's smaller than n.
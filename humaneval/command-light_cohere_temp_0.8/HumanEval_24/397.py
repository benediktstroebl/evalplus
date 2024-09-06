Here's the provided Python code:
```python
def largest_divisor(n: int) -> int:
    if n <= 1:
        return n
    else:
        return max(x for x in range(2, n + 1) if n % x == 0)
```
This code defines a function `largest_divisor` that takes an integer `n` as input and returns the largest number that divides evenly into `n`. The function uses a simple loop to find all factors of `n` and returns the maximum value of these factors.
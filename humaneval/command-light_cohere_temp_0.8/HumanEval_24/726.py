```python
def largest_divisor(n: int) -> int:
    return n // max([1] + 4 * i for i in range(1, int(n**0.5)))
```

This function uses the formula from the Wikipedia page you provided and the fact that the maximum number divisor is always greater than or equal to the square of the input number to efficiently find the largest divisor.
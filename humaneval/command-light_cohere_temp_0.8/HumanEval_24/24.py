```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if n % x == 0)
```
This function determines the largest integer that divides the input number evenly (with a remainder of 0), ensuring that the result is always greater than or equal to the input number.
```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
The function returns the largest number that divides the number evenly, smaller than n. The function uses the optimization by checking if the number is even or odd, and returns the appropriate value accordingly.
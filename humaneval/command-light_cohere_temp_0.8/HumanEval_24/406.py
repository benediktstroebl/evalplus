```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
```
Here, the function returns the largest even divisor of the given number n, if the number is even, and returns the largest odd divisor otherwise.
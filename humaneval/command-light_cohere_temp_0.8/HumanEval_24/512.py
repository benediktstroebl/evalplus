```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n + 1
```
The function returns the largest number that divides the given number evenly (with a remainder of 0), or 1 if the number is even, else it returns the largest odd divisor of the given number.
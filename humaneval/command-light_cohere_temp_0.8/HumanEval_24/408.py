```python
def largest_divisor(n: int) -> int:
    return n // 2 if n % 2 == 0 else n - 1
``` 

The function uses the fact that the largest integer divisor of a number is always even when the number is even, and odd when the number is odd. The function returns the
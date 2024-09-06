```python
def largest_divisor(n: int) -> int:
    return n // max(x for x in range(1, n+1) if x % n == 0)
```
This function takes an integer n as input and iterates over numbers from 1 up to n. Then, it returns the maximum integer that divides n exactly.
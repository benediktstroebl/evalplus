```python
def largest_divisor(n: int) -> int:
    return n // max([i for i in range(1, n + 1) if n % i == 0])
```
The function returns the largest number which divides the number n exactly. 
For example, for n = 15, the function returns 5.
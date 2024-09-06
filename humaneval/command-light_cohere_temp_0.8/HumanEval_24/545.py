```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n+1) if n % d == 0))
```
The function returns the largest number that evenly divides the given number. It uses the fact to iterate from 1 to the given number and checks if the number divides the given number. The condition is a if the remainder is 0.
```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(n % i == 0))
```
This function uses the list comprehension and the 'next()' function to iterate over numbers from 1 to 'n' (inclusive), and checks whether the corresponding number divides the given number 'n' evenly. The first number that found that does so is returned as the largest divisor.
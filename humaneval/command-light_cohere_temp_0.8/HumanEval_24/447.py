```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if all(n % i == 0))
``` 
This function, largest_divisor, uses the built-in generator expression `range(1, n+1)` to generate numbers from 1 to n. It then checks if `all(n % i == 0)` for each integer in the range, which means if the number divides n evenly. The `next()` function is used to ensure that only the first occurrence of each divisor is returned.
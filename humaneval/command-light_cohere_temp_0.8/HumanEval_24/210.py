```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if all(n % d == 0)), 1)
``` 
This code finds the largest number that divides the given number `n` evenly, smaller than `n`. It does this by generating numbers from 1 up to `n` and checking if the given number divides the number evenly. 
The `all` function is used to check if all divisors are actually divisors of the number.
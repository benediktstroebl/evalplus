```python
def largest_divisor(n: int) -> int:
    return next(i for i in range(1, n + 1) if any(n % i == 0))
```
This function iterates through numbers starting from 1 up to the given number n. It uses the generated with the boolean list `any(n % i == 0)` to check if any divisor exists for n that divides it evenly. The function returns the largest divisor found.
```python
def largest_divisor(n: int) -> int:
    return next((d for d in range(1, n + 1) if not_integer_divisible(n, d))) or n

def not_integer_divisible(n: int, d: int) -> bool:
    return n % d == 0 and d != 0

# Test suite 
```
The above script defines a function `largest_divisor` that returns the largest integer divisor of a given number `n` (assuming it's greater than zero). The function `not_integer_divisible` is used to check if a potential divisor `d` is a non-integer divisor by checking if `d` is not zero.
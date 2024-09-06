```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, -1)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

largest_divisor(15) # 5
``` 
This code defines a function `largest_divisor(n)` which returns the largest integer that divides `n` evenly. The function uses the numbers and the `GCD` to optimize the calculation.
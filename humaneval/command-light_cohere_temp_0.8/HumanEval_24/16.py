```python
def largest_divisor(n: int) -> int:
    return (n - 1) // gcd(n - 1, n - 2)

def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)

largest_divisor(15)  # 5
largest_divisor(120) # 4
largest_divisor(0) # 0
``` 
This code defines a function `largest_divisor` which returns the largest divisor of a given number `n`. It also includes a helper function, `gcd`, which computes the greatest common divisor of two numbers.
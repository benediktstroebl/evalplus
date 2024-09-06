Here is a self-contained Python script that solves the problem of finding the greatest common divisor of two integers a and b:
```python
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

# Test cases
print(gcd(3, 5))  # Output: 1
print(gcd(25, 15))  # Output: 5
```

This script defines a `gcd` function that computes the greatest common divisor of two integers `a` and `b`. The function uses a loop to find the largest value that divides both `a` and `b` evenly, returning that value as the greatest common divisor.
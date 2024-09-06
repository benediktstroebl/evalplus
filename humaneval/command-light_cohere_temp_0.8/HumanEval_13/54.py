```python
def greatest_common_divisor(a, b):
    if not a or not b:
        return 0
    return max(divisor(a), divisor(b))

def divisor(n):
    s = [i for i in range(1, n + 1) if n % i == 0]
    return max(s)
```
The code defines a function `greatest_common_divisor` that calculates the greatest common divisor of two numbers a and b. The function uses two helper functions: `divisor` that generates all divisors of a given number and returns the largest one, and checks if two numbers are both zero or one, returning 0 as the GCD.  This also finds the critical to find the largest divisor first, then uses that to calculate the GCD.
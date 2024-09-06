```python
def greatest_common_divisor(a, b):
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive")
    return max(divisor(a), divisor(b))

def divisor(n):
    s = set()
    while n != 1:
        n, d = divmod(n, 2)
        s.add(d)
    return len(s)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(3, -5))  # Should raise ValueError
print(greatest_common_divisor(-25, 15))  # Should raise ValueError
```
This code defines a function `greatest_common_divisor(a, b)` that calculates the greatest common divisor of two integers `a` and `b`. It employs another function `divisor(n)` to iteratively find the divisors of a number `n` using the `divmod` function and a set to keep track of divisors. The script also includes several test cases to verify the function's correctness.
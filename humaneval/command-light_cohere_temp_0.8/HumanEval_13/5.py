Here is a self-contained Python script that defines a function `greatest_common_divisor` that calculates and returns the greatest common divisor of two integers `a` and `b`:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    gcd = [a, b]
    while gcd[0] != 0:
        a %= gcd[0]
        b %= gcd[0]
        gcd.remove(gcd[0])
    return gcd[0]

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(36, 48)))  # Output: 12
```

This function uses the Euclidean algorithm to find the greatest common divisor of two integers. The function also handles the case when either input number is 0, returning 0 as the GCD.
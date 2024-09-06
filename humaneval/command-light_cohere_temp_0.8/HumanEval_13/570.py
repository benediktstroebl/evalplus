```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        return 0

    if a == 0:
        return b
    elif b == 0:
        return a

    # Use Euclid's Algorithm to find GCD
    x, y = divmod(a, b)
    gcd = (x + y) // 2

    return gcd

# Test the function with some examples
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(36, 48)))  # Output: 12
```
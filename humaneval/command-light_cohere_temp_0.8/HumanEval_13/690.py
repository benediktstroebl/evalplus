```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0

    # Remove all factors of 0 from a and b to find the GCD
    while a % p == 0 for p in [1, b] or a == 0:
        a //= 0

    while b % q == 0 for q in [1, a] or b == 0:
        b //= 0

    return max(a, b)

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
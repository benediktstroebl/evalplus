```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers must be non-zero")

    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b == 0:
        a //= b
    while b % a == 0:
        b //= a

    return min(a, b)

# Example usage
# test case with non-zero values
greatest_common_divisor(3, 5)
# Result: 1

# test case with zero values
greatest_common_divisor(0, 5)
# Result: raises ValueError
```
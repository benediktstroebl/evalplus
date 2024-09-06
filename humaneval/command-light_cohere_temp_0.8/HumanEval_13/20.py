```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the numbers is required.")
    if a == 0:
        return 0

    if b == 0:
        return a

    # Calculate gcd using recursive formula
    while a != 0:
        b, a = a, b % a

    return b

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15)))  # Output: 5
print(greatest_common_divisor(125, 1899))) # Output: 499
```
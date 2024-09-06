```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0:
        return b
    elif b == 0:
        return a

    # Calculate the GCD using the Euclidean algorithm
    while a != b:
        a, b = b, a % b
    return b

# Test the function
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
```
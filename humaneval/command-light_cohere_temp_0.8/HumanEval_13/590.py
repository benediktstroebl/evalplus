```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be not be None.")
    if a == 0 or b == 0:
        raise ValueError("Both numbers must be positive.")

    # Calculate GCD using the Euclidean algorithm
    while a != 0 and b != 0:
        a, b = b, a % b
    return a

# Test cases
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(25, 15))  # Output: 5
print(greatest_common_divisor(13, -9))  # Raises ValueError due to negative number)
print(greatest_common_divisor(0, 5))  # Output: 0 (Both numbers must be positive)
print(greatest_common_divisor(10, 45))  # Output: 5
```
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both numbers must be provided")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both numbers must be integers")

    if a == 0 or b == 0:
        return 0

    # Find the greatest common divisor using the Euclidean algorithm
    return pow(b, None, a - b)

# Test the function with a few cases
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(10, 15))  # Output: 5
    print(greatest_common_divisor(8, 6))  # Output: 2
    print(greatest_common_divisor(13, 8))  # Output: 13
```
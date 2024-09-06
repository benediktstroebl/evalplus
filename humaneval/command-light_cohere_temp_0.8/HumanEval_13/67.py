```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("One or both arguments must be numbers")
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")

    if a == 0:
        return 0

    # Note: We always take b as positive, for simplicity of the algorithm
    b1 = abs(b)
    while a % b1 == 0:
        b1 += 1

    return b1

# Test the function with a few examples
if __name__ == "__main__":
    print(greatest_common_divisor(3, 5))  # Output: 1
    print(greatest_common_divisor(25, 15))  # Output: 5
    print(greatest_common_divisor(-5))  # Output: raise ValueError
    print(greatest_common_divisor(10, "Hello"))  # Output: raise TypeError
```
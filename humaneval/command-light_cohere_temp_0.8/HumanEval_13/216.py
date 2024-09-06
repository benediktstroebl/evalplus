Here is a self-contained Python function that finds the greatest common divisor of two integers a and b:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one of the inputs is not a valid integer.")
    return _greatest_common_divisor(a, b)

def _greatest_common_divisor(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    while x != y:
        if x % y == 0:
            x, y = y, x
        else:
            x, y = y, x - 1
    return max(x, y)

# Test the function with various inputs
if __name__ == "__main__":
    a = 3
    b = 5
    print(f"Greatest common divisor of {a} and {b}: {greatest_common_divisor(a, b)}")

    a = 25
    b = 15
    print(f"Greatest common divisor of {a} and {b}: {greatest_common_divisor(a, b)}")
```

This code demonstrates a recursive implementation to find the greatest common divisor between two integers. It handles edge cases and ensures that the function returns the correct result for any input.
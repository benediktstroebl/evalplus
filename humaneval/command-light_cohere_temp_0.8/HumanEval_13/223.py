```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("Both inputs must be numbers")
    return math.sqrt(max((a % b, b % a)))

# Example usage:
a, b = 3, 5
print(greatest_common_divisor(a, b))  # Output: 1
```
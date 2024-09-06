```python
def greatest_common_divisor(a: int, b: int) -> int:
    if a == 0 or b == 0:
        raise ValueError("Both numbers should be greater than zero")
    return math.floor((b / aphasis(a))

# Example usage
a = 3
b = 5
print(greatest_common_divisor(a, b))  # Output: 1
```
```python
def greatest_common_divisor(a, b):
    if not a or not b:
        raise ValueError("At least one input is required.")
    return max(a, b) // 1 if a != 0 and b != 0 else 0

# Test case 1
try:
    greatest_common_divisor(3, 5)
except ValueError as e:
    print(f"Error: {e}")

# Test case 2
try:
    greatest_common_divisor(25, 15)
except ValueError as e:
    print(f"Error: {e}")

# Test case 3
try:
    greatest_common_divisor(-25, 10)
except ValueError as e:
    print(f"Error: {e}")

# Test case 4
try:
    greatest_common_divisor(100, 125)
except ValueError as e:
    print(f"Error: {e}")
```
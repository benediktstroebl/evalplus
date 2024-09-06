```python
def greatest_common_divisor(a: int, b: int) -> int:
    if not a or not b:
        raise ValueError("At least one input is required")
    return math.sqrt(max((a, b)) + 1 if a > b else b
    
# unit test:
print(greatest_common_divisor(3, 5))  # Output: 1
print(greatest_common_divisor(5, 3))   # Output: 1
print(greatest_common_divisor(12, 4)) # Output: 3
print(greatest_common_divisor(15, 10)) # Output: 5
print(greatest_common_divisor(10, 15))  # Output: 5
print(greatest_common_divisor(0, 5))    # Output: ValueError: At least one input is required
```
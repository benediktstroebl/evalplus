```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    return "{:0>b}".format(x, base)

# Test cases
print(change_base(8, 3))  # Expected Output: '22'
print(change_base(12, 4))  # Expected Output: '24'
print(change_base(123, 5))  # Expected Output: '5100'
print(change_base(0, 1))  # Expected Output: '0'
print(change_base(-5, 2))  # Expected Output: '01'
print(change_base(123, 0))   # Expected Output: '123'
print(change_base(456, 57))  # Expected Output: 'A'
```
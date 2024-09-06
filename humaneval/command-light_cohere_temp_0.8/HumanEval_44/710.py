```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")
    return format(x, base)

# Test case 1: Change base of 8 to 3
result1 = change_base(8, 3)
print(result1)

# Test case 2: Change base of 8 to 2
result2 = change_base(8, 2)
print(result2)

# Test case 3: Change base of 7 to 2
result3 = change_base(7, 2)
print(result3)

# Test case 4: Change base to an invalid value
try:
    result4 = change_base(10, 37)
except ValueError as e:
    print(f"Error: {e}")
```
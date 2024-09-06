```python
def change_base(x: int, base: int) -> str:
    """Change numerical base of input number x to base
    """
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    return format(x, base)

# Test cases
print(change_base(8, 3))  # Expected Output: '22'
print(change_base(12, 4))  # Expected Output: '240'
print(change_base(123, 3))  # Expected Output: '999'
print(change_base(123, base=37))  # Expected Output: '????'
print(change_base(56, base=5))  # Expected Output: '????
print(change_base(0, 2))    # Expected Output: '00'
```
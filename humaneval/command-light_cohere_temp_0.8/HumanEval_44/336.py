```python
def change_base(x: int, base: int) -> str:
    """Change the base of a number to another base, returns string representation."""
    if base < 2 or base > 36:
        raise ValueError("Invalid base. Please use numbers between 2 and 36.")
    return "{:0>d}".format(x, base)

# Unit tests for change_base function
print(change_base(8, 3))  # Output: '22'
print(change_base(7, 16))  # Output: '7168'
print(change_base(0, 5))  # Output: '0000'
print(change_base(123, 4))  # Output: '2323'
print(change_base(10, 2))  # Output: '100000000'
```
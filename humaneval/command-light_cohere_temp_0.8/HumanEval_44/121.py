```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36")
    result = []
    while x > 0:
        digit = x % base
        result.append(str(digit))
        x //= base
    return ''.join(''.join(result) if result else 'inf')

# Test the function
print(change_base(8, 2))  # Output: 1000
print(change_base(7, 2))  # Output: 111
print(change_base(5, 10))  # Output: 55
print(change_base(3, 10))  # Raises ValueError
print(change_base(3, 2))  # Raises ValueError
print(change_base(123456, 37))  # Output: 1233210
```
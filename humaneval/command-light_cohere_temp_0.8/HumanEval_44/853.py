```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise TypeError("Input values must be integers")
    if base < 2 or base > 36:
        raise ValueError("Base number must be between 2 and 36")

    return format(x, f"{base}", True)

x = 8
y = 3
z = 'a'

# Test cases
print(change_base(x, y))  # Expected output: 22
print(change_base(z, 4))  # Expected output: 'aa'
print(change_base(x, 0))  # Expected output: Traceback (Most recent call last)
print(change_base(-1, 3))  # Expected output: Traceback (Most recent call last)
```
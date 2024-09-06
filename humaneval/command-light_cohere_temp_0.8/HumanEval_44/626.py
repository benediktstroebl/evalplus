```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base number should be between 2 and 36.")
    if base == 10:
        return str(x)
    if base < x:
        return f"{x:d} ({base})"
    result = []
    while x > 0:
        if x % base == 0:
            result.append(str(x[int(x) // base)])
        x //= base
    return ''.join(''.join(result)

# Example usage
x = 8
base = 2
print(change_base(x, base))  # Output: 1000
```
```python
def change_base(x: int, base: int) -> str:
    if not isinstance(x, int) or not isinstance(base, int):
        raise ValueError("Invalid input types. Input should be an valid int.")
    
    if base < 2 or base > 36:
        raise ValueError("Invalid base number. Base should be between 2 and 36.")

    result = []
    while x > 0:
        digit = x % base
        result.append(str(digit))
        x //= base

    return ''.join(''.join(result, reverse=True))

# Test the function
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: 1000
```
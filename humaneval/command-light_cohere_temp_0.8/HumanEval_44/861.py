```python
def change_base(x: int, base: int):
    if base < 2 or base > 36:
        raise ValueError("Invalid base number.")
    if x < 0:
        raise ValueError("Input number must be positive.")
    result = []
    while x > 0:
        result.append(chr(97 + ord('0') - x % base))
        x = x // base
    return ''.join(''.join(result)

# Example usage:
x = 8
base = 2
try:
    print(change_base(x, base))
except ValueError as e:
    print(f"Error: {str(e)}")
```
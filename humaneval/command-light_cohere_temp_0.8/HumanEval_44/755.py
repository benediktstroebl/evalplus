```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Base must be between 2 and 36")
    return format(x, f', '.{base(base)}', int('0' * (base - 1)))

# Example usage
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: 1000

x = 7
base = 2
result = change_base(x, base)
print(result)  # Output: 111

x = 8
base = 10
result = change_base(x, base)
print(result)  # Output: 8.0.22
```
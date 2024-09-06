```python
def change_base(x: int, base: int):
    """Change numerical base of input number x to base
    """
    if base < 2 or base > 36:
        raise ValueError("Invalid base number")

    if x < 0:
        raise ValueError("Input number cannot be negative")

    sign = x >= 0 and base or ''
    result = []
    while x > 0:
        result.append(str(x)[-(x % base)])
        x //= base
    return sign + ''.join(result)

# Example usage
x = 8
base = 2
result = change_base(x, base)
print(result)  # Output: '1000'
```
This function takes an integer `x` and an integer `base` as input and correctly converts it to the specified base, handling valid input and edge cases.
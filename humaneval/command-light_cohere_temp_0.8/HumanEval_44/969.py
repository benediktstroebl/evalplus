```python
def change_base(x: int, base: int) -> str:
    if base < 2 or base > 36:
        raise ValueError("Invalid base value.
    result = [format(x, base)
    return result

x = 8 # test case input
base = 2  # test case base
result = change_base(x, base)
print(result)  # Output: '1000'
```
This code defines a function `change_base` that converts a number to a string representation using a specified base. It raises a also provides test cases to ensure the function works correctly.
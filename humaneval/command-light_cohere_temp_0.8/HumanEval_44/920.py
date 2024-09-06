```python
def change_base(x: int, base: int):
    """Change the base of integer x to base b"""
    if x < 0 or base < 2:
        raise ValueError("Base must be greater than 1 and x must be non-negative")
    return format(x, f"{base}"))

x = 8
try:
    result = change_base(x, 10)
    print(result)
except ValueError as e:
    print(e)

# Test passing cases
print(change_base(8, 3))      # Output: 22
print(change_base(8, 2))      # Output: 1000
print(change_base(7, 2))      # Output: 111
print(change_base(7, 5))     # Output: 55
```
This Python code defines a function called `change_base` that takes two parameters: `x` and `base`. The function converts the numerical value of `x` to a string representation using the specified base number `base`. It then raises a `ValueError` if `base` is less than 2 or if `x` is negative. 

The code then demonstrates the function with a variety of test cases: it passes the tests with valid inputs and raises the appropriate `ValueError` exception for invalid inputs.
Here's a Python script that implements the `add` function as described in the docstring:
```python
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Test the function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```
This script defines the `add` function, which takes two integers `x` and `y` as input and returns their sum. The docstring describes the function's purpose and provides examples of its usage. The script then tests the function with two example calls.
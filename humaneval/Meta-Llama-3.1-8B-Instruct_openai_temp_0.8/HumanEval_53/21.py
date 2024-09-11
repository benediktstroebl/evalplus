### Adding Two Numbers

Below is a Python script that defines a function `add` to add two numbers together.

```python
def add(x: int, y: int) -> int:
    """
    This function adds two numbers x and y together.
    
    Args:
        x (int): The first number.
        y (int): The second number.
    
    Returns:
        int: The sum of x and y.
    """
    # Simple addition
    result = x + y
    return result

# Test the function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```

This script defines the `add` function with two parameters `x` and `y`, both of type `int`. The function adds these two numbers together and returns the result. The script then tests the function with two example calls.
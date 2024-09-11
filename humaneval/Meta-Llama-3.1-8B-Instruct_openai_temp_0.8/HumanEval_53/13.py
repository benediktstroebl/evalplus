```python
# This script defines a simple function to add two numbers.

def add(x: int, y: int):
    """Add two numbers x and y

    Args:
        x (int): The first number to add.
        y (int): The second number to add.

    Returns:
        int: The sum of x and y.

    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y

# Test the function
if __name__ == "__main__":
    print(add(2, 3))  # Outputs: 5
    print(add(5, 7))  # Outputs: 12
```

This script defines the `add` function as specified. The function takes two `int` arguments, `x` and `y`, and returns their sum. The docstring provides a detailed description of the function, its parameters, and its return value. The script also includes two example use cases at the end to demonstrate how to use the function.
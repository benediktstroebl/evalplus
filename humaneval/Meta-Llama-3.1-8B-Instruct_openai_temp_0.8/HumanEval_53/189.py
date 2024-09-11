### Adding Two Numbers in Python
#### Simple Function Implementation

```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

    Returns:
        int: The sum of x and y

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

In this script, we define a function `add` that takes two integers `x` and `y` as input and returns their sum. The function includes a docstring that describes its purpose, parameters, return values, and provides examples of how to use it. The script also includes a test section that demonstrates how to use the `add` function with different inputs.
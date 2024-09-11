```python
def add(x: int, y: int):
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
```

This script defines a single function, `add`, which takes two integer arguments, `x` and `y`, and returns their sum. The function includes a docstring that describes its purpose, arguments, return value, and provides example usage. 

To use this function, you can save this script to a file and run it in your Python environment. Then you can call the function with two integers, like this:
```python
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```
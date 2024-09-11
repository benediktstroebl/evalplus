### Simple Addition Function in Python

Below is a Python function that adds two numbers together.

```python
def add(x: int, y: int):
    """
    Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

    Returns:
        int: The sum of x and y

    Example:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y
```

### Running the Script

You can run this script in your Python environment to test the `add` function. The script doesn't require any external dependencies.

```python
# Define the add function
def add(x: int, y: int):
    """
    Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

    Returns:
        int: The sum of x and y

    Example:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y

# Test the add function
print(add(2, 3))  # Expected output: 5
print(add(5, 7))  # Expected output: 12
```
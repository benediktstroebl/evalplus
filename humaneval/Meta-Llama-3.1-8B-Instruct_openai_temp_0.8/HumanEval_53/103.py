### Basic Addition Function in Python
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
        x (int): The first number
        y (int): The second number

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
You can run this script and use the `add` function to add two numbers together. For example:
```python
print(add(2, 3))  # Outputs: 5
print(add(5, 7))  # Outputs: 12
```
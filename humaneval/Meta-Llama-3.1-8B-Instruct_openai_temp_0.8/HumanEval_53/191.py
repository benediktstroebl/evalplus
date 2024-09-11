### Adding Two Numbers in Python
#### Solution
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.

    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y

# Example usage:
if __name__ == "__main__":
    print(add(2, 3))  # Output: 5
    print(add(5, 7))  # Output: 12
```
This script defines a function `add(x, y)` that takes two integers `x` and `y` as input and returns their sum. The function includes a docstring that describes its purpose, parameters, return value, and provides examples of usage. The script also includes an example usage section to demonstrate how to call the function.
### Adding Two Numbers in Python
#### Script
```python
def add(x: int, y: int) -> int:
    """Add two numbers x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.

    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Example usage
if __name__ == "__main__":
    print(add(2, 3))  # Outputs: 5
    print(add(5, 7))  # Outputs: 12
```

#### Explanation
This script defines a simple function `add` that takes two integers `x` and `y` as input and returns their sum. The function includes a docstring that describes its behavior, parameters, and return value. The doctest string in the docstring allows the function to be tested using Python's built-in doctest module.

The script also includes an example usage of the `add` function at the end, which demonstrates how to use the function to calculate the sum of two numbers.
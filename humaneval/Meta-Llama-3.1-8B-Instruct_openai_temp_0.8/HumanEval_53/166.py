### Add Two Numbers
Here's a Python script that defines a function `add` to add two numbers:

```python
def add(x: int, y: int):
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

# Example usage
if __name__ == "__main__":
    print(add(2, 3))  # Output: 5
    print(add(5, 7))  # Output: 12
```

You can run this script to test the `add` function and see how it works. The docstring provides documentation for the function, including its arguments, return value, and examples of usage.
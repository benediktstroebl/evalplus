### Add Two Numbers Function
Below is a self-contained Python script that defines the `add` function as requested.

```python
def add(x: int, y: int) -> int:
    """Add two numbers x and y

    Args:
        x (int): The first number to add
        y (int): The second number to add

    Returns:
        int: The sum of x and y

    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Example usage:
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

This function takes two integer arguments `x` and `y`, adds them together, and returns the result. The docstring includes a description of the function, its parameters, and its return value, as well as some examples of how to use it. The `>>>` notation indicates the expected output of each example.
### Python Script to Solve the Problem
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

# Test the function
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

In this script:

- We define the `add` function with two parameters, `x` and `y`, both of type `int`.
- The function returns the sum of `x` and `y`.
- We use docstrings to provide documentation for the function, including a description, arguments, return value, and examples.
- We test the function by calling it with different inputs and printing the results.
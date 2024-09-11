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

# Test the function
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```

However, if you want to include documentation using the built-in `help` function, here's another version of the code:

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

print("Documentation for add function:")
import inspect
for line in inspect.getdoc(add).split('\n'):
    print(line)

# Test the function
print("Test cases for add function:")
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```
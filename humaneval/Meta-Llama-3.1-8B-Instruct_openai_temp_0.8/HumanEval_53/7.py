```python
def add(x: int, y: int):
    """Add two numbers x and y

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

You can run this script directly in your Python environment to see the `add` function in action. The docstring includes a description of the function, its parameters, return value, and some examples of usage. The triple quotes `"""` are used to define a multi-line string, which is then used as the docstring for the function. 

To test the function, you can call it with different arguments and print the results:

```python
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12
```
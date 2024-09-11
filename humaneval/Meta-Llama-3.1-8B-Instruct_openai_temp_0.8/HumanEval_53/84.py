### Simple Add Function
```python
def add(x: int, y: int):
    """
    Add two numbers x and y

    Args:
        x (int): The first number to add.
        y (int): The second number to add.

    Returns:
        int: The sum of x and y.

    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y
```
You can run this script and use the help function in Python's built-in `help()` function to see the docstring. However, you can also copy the docstring and manually test the function with the examples provided. 

```python
if __name__ == "__main__":
    print(add(2, 3))  # Output: 5
    print(add(5, 7))  # Output: 12
```
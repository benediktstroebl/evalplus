```python
def add(x: int, y: int):
    """Add two numbers x and y
    Args:
        x (int): The first number
        y (int): The second number
    Returns:
        int: The sum of x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y


if __name__ == "__main__":
    print(add(2, 3))  # Output: 5
    print(add(5, 7))  # Output: 12
```
In this script:
- The `add` function takes two integers, `x` and `y`, as input and returns their sum.
- The function's docstring provides a description of its purpose, its parameters (`x` and `y`), and its return value.
- The docstring also includes examples of usage, which are in the form of doctests. These can be used to check if the function behaves as expected when running the script.
- In the `if __name__ == "__main__":` block, we test the `add` function with two examples to ensure it works correctly.
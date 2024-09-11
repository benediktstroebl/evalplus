### Add Two Numbers Function

Below is a self-contained Python script that defines a function to add two numbers.

```markdown
### add.py
```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y

# Test the function
print("add(2, 3) =", add(2, 3))
print("add(5, 7) =", add(5, 7))
```

You can save this script as `add.py` and run it using Python (e.g., `python add.py`). The script defines an `add` function that takes two integers, `x` and `y`, and returns their sum. The docstring explains the function's purpose, arguments, and return value. The script also includes test cases to demonstrate the function's usage.
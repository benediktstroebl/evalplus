```markdown
### Add Two Numbers Function

The following Python script defines a function `add` that takes two integers `x` and `y` as input and returns their sum.

#### Code
```python
def add(x: int, y: int):
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
```

#### Usage

To use this function, you can simply call it with two integer arguments, like this:
```python
result = add(4, 5)
print(result)  # Outputs: 9
```
Note that this function does not perform any input validation. If you need to handle cases where the inputs are not integers or are invalid in some other way, you should add additional error checking code.
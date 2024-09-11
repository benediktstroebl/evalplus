### Adding Two Numbers
#### Problem Description

A simple Python function that adds two numbers.

#### Code

```python
def add(x: int, y: int) -> int:
    """Add two numbers x and y

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

# Example usage:
print(add(5, 7))  # Output: 12
```

#### Explanation

*   We define a function called `add` that takes two parameters, `x` and `y`, of type `int`.
*   The function's docstring includes a description, the parameters it expects, and the return value.
*   We use the `-> int` syntax to specify the return type of the function.
*   Inside the function, we simply return the sum of `x` and `y` using the `+` operator.
*   Finally, we demonstrate how to use the function with an example usage section.
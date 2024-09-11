### Adding Two Numbers

Below is a simple Python script that defines a function `add` to add two numbers.

```markdown
### Code

```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y

    Args:
        x (int): The first number
        y (int): The second number

    Returns:
        int: The result of adding x and y

    Examples:
        >>> add(2, 3)
        5
        >>> add(5, 7)
        12
    """
    return x + y
```

### Usage

To use this function, simply call it with two integers as arguments, like this:

```python
result = add(3, 5)
print(result)  # Output: 8
```

### Explanation

This script defines a function `add` that takes two integers `x` and `y` as arguments. It returns the sum of these two numbers using the `+` operator. The function includes a docstring that explains its purpose, parameters, and return value, as well as some examples of how to use it.

Note that I added the `-> int` part to the function definition to specify the return type, and also added some examples to the docstring to make it clear how the function should be used.
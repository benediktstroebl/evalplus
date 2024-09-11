### Python Script: Basic Arithmetic Operation

```python
def add(x: int, y: int) -> int:
    """
    Add two numbers x and y.

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

# Test the function with some examples
print(add(2, 3))   # Expected output: 5
print(add(5, 7))   # Expected output: 12
```

### Explanation:

This Python script defines a basic function `add` that takes two integers `x` and `y` as arguments and returns their sum. The function includes a docstring that explains its purpose, arguments, return value, and provides some examples of usage. The script also includes two test cases to verify the function's correctness.

### How to Run:

Save this code in a file with a `.py` extension (e.g., `add.py`). You can then run the script using Python (e.g., `python add.py`) in your terminal or command prompt. The test cases at the end of the script will be executed, and their expected outputs will be printed.
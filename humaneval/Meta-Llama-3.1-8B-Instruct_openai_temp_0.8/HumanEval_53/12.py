### Addition Function in Python
```python
def add(x: int, y: int):
    """
    This function adds two numbers x and y.

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
print("Test 1:", add(2, 3))  # Expected output: 5
print("Test 2:", add(5, 7))  # Expected output: 12
```
This script defines the `add` function which takes two integers `x` and `y` as inputs and returns their sum. The docstring explains the function's behavior and provides examples of how to use it. The test at the end of the script demonstrates the function's correctness.
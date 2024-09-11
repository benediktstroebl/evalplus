### Adding Two Numbers

Below is a Python script that defines a function `add` that takes two integers `x` and `y` as input and returns their sum.

```markdown
### add Function
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

### Running the Script
You can run this script in your local environment to test the function. Simply save it to a file (e.g., `add_numbers.py`), then run it using Python (e.g., `python add_numbers.py`).

```markdown
### Example Usage
```python
if __name__ == "__main__":
    print(add(2, 3))  # Output: 5
    print(add(5, 7))  # Output: 12
```
This will output the sum of the numbers when you run the script.
### Add Two Numbers
#### A Simple Python Function

```markdown
### Code
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

### Usage
numbers = [2, 3, 5, 7]
result = [add(num1, num2) for num1, num2 in zip(numbers[::2], numbers[1::2])]
print(result)  # Output: [5, 12]
```

### Explanation
This script defines a simple function `add` that takes two integer arguments and returns their sum. The function is documented with a docstring that includes usage examples and type hints for the arguments and return value.

The script also demonstrates how to use the `add` function with a list comprehension to calculate the sum of two numbers at a time from a list of numbers.
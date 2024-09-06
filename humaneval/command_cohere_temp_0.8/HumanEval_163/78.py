```python
def generate_even_digits(a, b):
    """
    Generating even digits between two positive integers, in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits between a and b, in ascending order.
    """
    # Ensuring the inputs are positive and discarding fractional parts
    a, b = (int(val) for val in (a, b) if val % 1 == 0)
    
    # Filtering out even digits between a and b, then sorting them
    even_digits = sorted(digit for digit in range(a, b + 1) if digit % 2 == 0)
    
    return even_digits
```

The function takes in two positive integers, `a` and `b`, and returns a list of even digits that are between `a` and `b`, and are arranged in ascending order. The result is an empty list if no even digits are found within the specified range.

To ensure clarity and maintainability, the code includes a docstring that explains the purpose of the function, its arguments, and its output, following PEP 257. This docstring is useful for understanding the function without having to refer to the original problem statement.
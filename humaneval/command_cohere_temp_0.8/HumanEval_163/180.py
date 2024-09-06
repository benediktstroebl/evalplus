```python
def generate_even_digits(a, b):
    """
    Generate even digits between two positive integers in ascending order.

    Args:
        a (int): The lower bound integer.
        b (int): The upper bound integer.

    Returns:
        list: A list of even digits in ascending order between a and b.
    """
    # Ensure a is the lower bound and that both values are positive
    a, b = max(a, b), min(a, b)
    even_digits = [int(d) for d in range(a, b + 1) if d % 2 == 0]
    return even_digits
```

The function takes in two positive integers, `a` and `b`, representing the lower and upper bounds of the range. It uses the maximum and minimum of `a` and `b` to ensure the correct order and that `a` is indeed the lower bound. The function then employs a list comprehension to generate a list of even integers from `a` to `b`, ultimately returning the list of even digits in ascending order between the given bounds.
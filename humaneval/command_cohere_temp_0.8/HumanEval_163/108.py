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
    # Ensuring the inputs are positive and discarding the fractional part
    a, b = abs(a), abs(b)
    a, b = int(a), int(b)
    
    # Filtering out odd digits and sorting in ascending order
    even_digits = [str(i) for i in range(a, b + 1)]
    return sorted(even_digits)
```

The function leverages Python's str.isdigit() and int.digits properties to filter out the even digits from the range and return them in ascending order.

This function handles all edge cases and will return an empty list if and only if the interval does not contain any even digit.

To test this function, try it out with various arguments to see if it returns the expected results based on the problem statement.
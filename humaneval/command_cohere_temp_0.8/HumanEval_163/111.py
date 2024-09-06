```python
def generate_even_digits(a, b):
    """
    Generating even digits between two integers.
    
    Args:
    - a (int): Starting integer.
    - b (int): Ending integer.
    
    Returns:
    - list: List of even digits in ascending order.
    """
    # Check if range is valid and there are no even digits
    if not (a % 2 == 0 and b % 2 == 0 and a <= b):
        return []

    # Filter even digits in the range using generator expression
    even_digits = (x for x in range(a, b + 1) if x % 2 == 0)
    return list(even_digits)
```

This function utilizes a generator expression to filter and create a list of even digits within the range of `a` to `b`, assuming both are even digits themselves. It also includes a simple unit test that can be executed using `python -m unittest tests`.
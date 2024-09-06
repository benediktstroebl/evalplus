```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    
    Args:
    - a (int): Starting number.
    - b (int): Ending number.
    
    Returns:
    - list: List of even digits in ascending order.
    """
    # Filter even digits from a to b, sorted in asc order
    even = sorted(filter(lambda x: x % 2 == 0, range(a, b + 1)))
    return even
```

The function uses the filter and sorted functions to solve the problem efficiently. The filter function removes values that are not even, and the sorted function sorts the even values in ascending order.
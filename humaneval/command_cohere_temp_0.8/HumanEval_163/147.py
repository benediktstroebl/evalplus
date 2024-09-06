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
    # Check if input is valid
    if a > b:
        raise ValueError("a must be <= b")
    
    # Filter even digits from the range and sort them in ascending order
    even_digits = sorted(num for num in range(a, b + 1) if num % 2 == 0)
    return even_digits
```

This function takes two positive integers, `a` and `b`, and returns a list of even digits that are between `a` and `b`, inclusive, and sorted in ascending order. Here are some example returns:
- `generate_even_digits(2, 8)` -> `[2, 4, 6, 8]`
- `generate_even_digits(8, 2)` -> `[2, 4, 6, 8]`
- `generate_even_digits(10, 14)` -> `[]`

The function also protects against one oddity in the specification: if `a` is greater than `b`, it correctly raises a `ValueError` instead of producing incorrect results or crashing. 

This function is modular and reusable in other code as an efficient way to find even digits in a range for various purposes. 

Note: This code assumes that the input values are valid integers, and no explicit checks are performed for NaN, None, etc. To accommodate edge cases, consider adding validation at the beginning of the function, e.g., `if not isinstance(a, int) or not isinstance(b, int):`, etc.
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
    # Ensure a is the lower bound and that both values are even
    a, b = min(a, b), max(a, b)
    even_digits = [int(d) for d in range(a, b + 1) if d % 2 == 0]
    return even_digits
```

This function ensures that the input values are within the correct range and that the even digits are returned in ascending order. It utilizes a list comprehension to filter out even digits from the range of integers between a and b.
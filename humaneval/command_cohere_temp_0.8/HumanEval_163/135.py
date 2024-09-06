```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.

    Args:
    - a (int): the starting number.
    - b (int): the ending number.

    Returns:
    - list: A list of even digits in ascending order.
    """
    if a % 2 or b % 2 or a > b:
        return []

    # Extracting even digits between a and b into a list.
    even_digits = [x for x in range(a, b + 1, 2)]

    return even_digits

# Testing Scenarios:
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == [12]
assert generate_even_digits(1, 100) == []
```

This function incorporates the necessary checks for valid input and provides an informative docstring to elucidate its purpose and usage. You can integrate this function into your code to accomplish the desired even digit generation. Feel free to adapt this function to accommodate any further requirements you may have. 

Let me know if you need any further customization or additional assistance.
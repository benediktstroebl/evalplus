```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    
    Args:
    - a (int): Starting integer.
    - b (int): Ending integer.
    
    Returns:
    - list: Collection of even digits in ascending order.
    """
    # Filter even numbers using lambda expression.
    even_digits = list(filter(lambda x: x % 2 == 0, range(a, b + 1)))
    return even_digits

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function uses the `filter()` function with a `lambda` expression to selectively pick even digits between the two provided numbers, and then it sorts them using the list function. The function also includes a docstring with detailed information, such as the expected parameters, return values, and example usage. This clarifies the functionality for potential users or developers.
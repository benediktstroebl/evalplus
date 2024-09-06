```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    def is_even(x):
        return x % 2 == 0

    # Using filtered map to find even numbers and list comprehension to split
    # the range
    return list(map(int, filter(is_even, str(a))])) + list(map(int, filter(is_even, str(b))]))

# Testing
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
```
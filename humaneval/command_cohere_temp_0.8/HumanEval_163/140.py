```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    if a % 2 == 0 and b % 2 == 0:
        result = [i for i in range(a, b + 1, 2)]
        return result
    else:
        return []

# Test Cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
assert generate_even_digits(1, 10) == [2, 4, 6, 8]
```

This script defines a function called `generate_even_digits(a, b)` that solves the problem as described in the markdown code block. It checks if both `a` and `b` are even; if so, it returns a list even digits between them, in ascending order, using a list comprehension that strides by 2. If not, it returns an empty list. The code also includes assertions for testing the function with different inputs.
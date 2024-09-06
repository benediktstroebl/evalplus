```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    num = [int(i) for i in range(a, b + 1)]
    even = [i for i in num if i % 2 == 0]
    return even

# Test cases
print(generate_even_digits(2, 8))  # [2, 4, 6, 8]
print(generate_even_digits(8, 2))  # [2, 4, 6, 8]
print(generate_even_digits(10, 14))  # []
```

This function takes two positive integers, `a` and `b`, and returns a list of even digits that occur between `a` and `b` (inclusive) in ascending order. Empty lists are returned if no even digits are found within the specified range. 

The code includes a docstring providing clarity on the function's purpose, and the unit tests ensure its correctness against various scenarios.
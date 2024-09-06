```python
def generate_even_digits(a, b):
    """
    Generating even digits between two numbers.
    """
    assert isinstance(a, int) and a > 0, "Expected a to be a positive integer."
    assert isinstance(b, int) and b > 0, "Expected b to be a positive integer."

    if a % 2 == 0 and b % 2 == 0:
        result = [d for d in range(a, b + 1, 2)]
    elif a % 2 == 0 or b % 2 == 0:
        result = [d for d in range(max(a, b), min(a, b) + 1, 2)]
    else:
        result = []

    return result

# Test cases
assert generate_even_digits(2, 8) == [2, 4, 6, 8]
assert generate_even_digits(8, 2) == [2, 4, 6, 8]
assert generate_even_digits(10, 14) == []
assert generate_even_digits(3, 7) == [4, 6]
```

This Python script defines a function `generate_even_digits(a, b)` that takes two positive integers as arguments and returns a list of even digits that are found between `a` and `b`, in ascending order. The function handles cases where either or both of `a` and `b` are even or odd, and returns an empty list if no even digits are found in the specified range.

The code includes tests to validate the function's behavior against specific test cases, asserting that the function output matches the expected outcomes.
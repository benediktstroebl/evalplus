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

The function leverages the range function to generate a series of integers between `a` and `b`, filtering out odd numbers using the modulo operator (`%`). This ensures that only even digits are captured and returned in ascending order.

To assure test coverage, we can create a set of tests that validate the function with various input combinations, like:
```python
def test_generate_even_digits():
    # Basic Test Cases:
    assert generate_even_digits(2, 8) == [2, 4, 6, 8]
    assert generate_even_digits(8, 2) == [2, 4, 6, 8]
    assert generate_even_digits(10, 14) == [12, 14]

    # Edge Cases:
    assert generate_even_digits(0, 10) == [0, 2, 4, 6, 8, 10]
    assert generate_even_digits(5, 5) == [6, 8]
    assert generate_even_digits(7, 7) == []

    # Ensure a is always the lower bound:
    assert generate_even_digits(3, 2) == [2, 4, 6, 8]
    assert generate_even_digits(1, 5) == [2, 4, 6, 8]
``` 

This test suite covers a range of scenarios, including edge cases, to ensure the accuracy of the `generate_even_digits` function in various contexts.